# -*- coding: utf-8 -*-
import logging


from django.db.transaction import atomic
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from networkapi.api_ip import facade as facade_v3
from networkapi.api_ip.permissions import Read
from networkapi.api_ip.permissions import Write
from networkapi.api_ip.permissions import write_objv4_permission
from networkapi.api_ip.permissions import write_objv6_permission
from networkapi.api_ip.v4 import serializers
from networkapi.api_ip.v4 import tasks
from networkapi.settings import SPECS
from networkapi.util.classes import CustomAPIView
from networkapi.util.decorators import logs_method_apiview
from networkapi.util.decorators import permission_classes_apiview
from networkapi.util.decorators import permission_obj_apiview
from networkapi.util.decorators import prepare_search
from networkapi.util.geral import render_to_json
from networkapi.util.json_validate import json_validate
from networkapi.util.json_validate import raise_json_validate

log = logging.getLogger(__name__)


class IPv4V4View(CustomAPIView):

    @logs_method_apiview
    @raise_json_validate('')
    @permission_classes_apiview((IsAuthenticated, Read))
    @prepare_search
    def get(self, request, *args, **kwargs):
        """Returns a list of vip request by ids ou dict."""

        if not kwargs.get('obj_ids'):
            obj_model = facade_v3.get_ipv4_by_search(self.search)
            ips = obj_model['query_set']
            only_main_property = False
        else:
            obj_ids = kwargs.get('obj_ids').split(';')
            ips = facade_v3.get_ipv4_by_ids(obj_ids)
            only_main_property = True
            obj_model = None

        # serializer ips
        serializer_ip = serializers.IPv4V4Serializer(
            ips,
            many=True,
            fields=self.fields,
            include=self.include,
            exclude=self.exclude,
            kind=self.kind
        )

        # prepare serializer with customized properties
        data = render_to_json(
            serializer_ip,
            main_property='ips',
            obj_model=obj_model,
            request=request,
            only_main_property=only_main_property
        )

        return Response(data, status=status.HTTP_200_OK)

    @logs_method_apiview
    @raise_json_validate('ipv4_post_v4')
    @permission_classes_apiview((IsAuthenticated, Write))
    @permission_obj_apiview([write_objv4_permission])
    @atomic
    def post(self, request, *args, **kwargs):
        """Create Ipv4."""

        ips = request.DATA
        json_validate(SPECS.get('ipv4_post_v4')).validate(ips)
        response = list()
        for ip in ips['ips']:
            if 'reserve_all' in ip and ip['reserve_all'] is True:
                ret = facade_v3.create_ipv4(ip, request.user, reserve_all=ip['reserve_all'])
            else:
                ret = facade_v3.create_ipv4(ip, request.user)
            response.append({'id': ret.id})

        return Response(response, status=status.HTTP_201_CREATED)

    @logs_method_apiview
    @raise_json_validate('ipv4_put_v4')
    @permission_classes_apiview((IsAuthenticated, Write))
    @permission_obj_apiview([write_objv4_permission])
    @atomic
    def put(self, request, *args, **kwargs):
        """Edit Ipv4."""

        ips = request.DATA
        json_validate(SPECS.get('ipv4_put_v4')).validate(ips)
        response = list()
        for ip in ips['ips']:
            ret = facade_v3.update_ipv4(ip, request.user)
            response.append({'id': ret.id})

        return Response(response, status=status.HTTP_200_OK)

    @logs_method_apiview
    @raise_json_validate('')
    @permission_classes_apiview((IsAuthenticated, Write))
    @permission_obj_apiview([write_objv4_permission])
    @atomic
    def delete(self, request, *args, **kwargs):
        """Delete Ipv4."""

        obj_ids = kwargs['obj_ids'].split(';')

        for obj_id in obj_ids:
            facade_v3.delete_ipv4(obj_id)

        return Response({}, status=status.HTTP_200_OK)


class IPv4V4AsyncView(CustomAPIView):

    @logs_method_apiview
    @raise_json_validate('ipv4_post_v4')
    @permission_classes_apiview((IsAuthenticated, Write))
    @permission_obj_apiview([write_objv4_permission])
    @atomic
    def post(self, request, *args, **kwargs):
        """Create Ipv4."""

        response = list()
        ips = request.DATA
        json_validate(SPECS.get('ipv4_post_v4')).validate(ips)

        user = request.user

        for ip in ips['ips']:
            task_obj = tasks.create_ipv4.apply_async(args=[ip, user.id],
                                                     queue='napi.network')

            task = {
                'task_id': task_obj.id
            }

            response.append(task)

        return Response(response, status=status.HTTP_202_ACCEPTED)

    @logs_method_apiview
    @raise_json_validate('ipv4_put_v4')
    @permission_classes_apiview((IsAuthenticated, Write))
    @permission_obj_apiview([write_objv4_permission])
    @atomic
    def put(self, request, *args, **kwargs):
        """Edit Ipv4."""

        response = list()
        ips = request.DATA
        json_validate(SPECS.get('ipv4_put_v4')).validate(ips)

        user = request.user

        for ip in ips['ips']:
            task_obj = tasks.update_ipv4.apply_async(args=[ip, user.id],
                                                     queue='napi.network')

            task = {
                'task_id': task_obj.id
            }

            response.append(task)

        return Response(response, status=status.HTTP_202_ACCEPTED)

    @logs_method_apiview
    @raise_json_validate('')
    @permission_classes_apiview((IsAuthenticated, Write))
    @permission_obj_apiview([write_objv4_permission])
    @atomic
    def delete(self, request, *args, **kwargs):
        """Delete Ipv4."""

        response = list()
        obj_ids = kwargs['obj_ids'].split(';')

        user = request.user

        for obj_id in obj_ids:
            task_obj = tasks.delete_ipv4.apply_async(
                args=[obj_id, user.id], queue='napi.network')

            task = {
                'task_id': task_obj.id
            }

            response.append(task)

        return Response(response, status=status.HTTP_202_ACCEPTED)


class IPv6V4View(CustomAPIView):

    @logs_method_apiview
    @permission_classes_apiview((IsAuthenticated, Read))
    @prepare_search
    def get(self, request, *args, **kwargs):

        if not kwargs.get('obj_ids'):
            obj_model = facade_v3.get_ipv6_by_search(self.search)
            ips = obj_model['query_set']
            only_main_property = False
        else:
            obj_ids = kwargs.get('obj_ids').split(';')
            ips = facade_v3.get_ipv6_by_ids(obj_ids)
            only_main_property = True
            obj_model = None

        # serializer ips
        serializer_ip = serializers.Ipv6V4Serializer(
            ips,
            many=True,
            fields=self.fields,
            include=self.include,
            exclude=self.exclude,
            kind=self.kind
        )

        # prepare serializer with customized properties
        data = render_to_json(
            serializer_ip,
            main_property='ips',
            obj_model=obj_model,
            request=request,
            only_main_property=only_main_property
        )

        return Response(data, status=status.HTTP_200_OK)

    @logs_method_apiview
    @raise_json_validate('ipv6_post_v4')
    @permission_classes_apiview((IsAuthenticated, Write))
    @permission_obj_apiview([write_objv6_permission])
    @atomic
    def post(self, request, *args, **kwargs):
        """Save Ipv6."""

        ips = request.DATA
        json_validate(SPECS.get('ipv6_post_v4')).validate(ips)
        response = list()
        for ip in ips['ips']:
            ret = facade_v3.create_ipv6(ip, request.user)
            response.append({'id': ret.id})

        return Response(response, status=status.HTTP_201_CREATED)

    @logs_method_apiview
    @raise_json_validate('ipv6_put_v4')
    @permission_classes_apiview((IsAuthenticated, Write))
    @permission_obj_apiview([write_objv6_permission])
    @atomic
    def put(self, request, *args, **kwargs):
        """Edit Ipv6."""

        ips = request.DATA
        json_validate(SPECS.get('ipv6_put_v4')).validate(ips)
        response = list()
        for ip in ips['ips']:
            ret = facade_v3.update_ipv6(ip, request.user)
            response.append({'id': ret.id})

        return Response(response, status=status.HTTP_200_OK)

    @logs_method_apiview
    @raise_json_validate('')
    @permission_classes_apiview((IsAuthenticated, Write))
    @permission_obj_apiview([write_objv6_permission])
    @atomic
    def delete(self, request, *args, **kwargs):
        """Edit Ipv6"""

        obj_ids = kwargs['obj_ids'].split(';')

        for obj_id in obj_ids:
            facade_v3.delete_ipv6(obj_id)

        return Response({}, status=status.HTTP_200_OK)


class IPv6V4AsyncView(CustomAPIView):

    @logs_method_apiview
    @raise_json_validate('ipv6_post_v4')
    @permission_classes_apiview((IsAuthenticated, Write))
    @permission_obj_apiview([write_objv6_permission])
    @atomic
    def post(self, request, *args, **kwargs):
        """Create Ipv6."""

        response = list()
        ips = request.DATA
        json_validate(SPECS.get('ipv6_post_v4')).validate(ips)

        user = request.user

        for ip in ips['ips']:
            task_obj = tasks.create_ipv6.apply_async(args=[ip, user.id],
                                                     queue='napi.network')

            task = {
                'task_id': task_obj.id
            }

            response.append(task)

        return Response(response, status=status.HTTP_202_ACCEPTED)

    @logs_method_apiview
    @raise_json_validate('ipv6_put_v4')
    @permission_classes_apiview((IsAuthenticated, Write))
    @permission_obj_apiview([write_objv6_permission])
    @atomic
    def put(self, request, *args, **kwargs):
        """Edit Ipv6."""

        response = list()
        ips = request.DATA
        json_validate(SPECS.get('ipv6_put_v4')).validate(ips)

        user = request.user

        for ip in ips['ips']:
            task_obj = tasks.update_ipv6.apply_async(args=[ip, user.id],
                                                     queue='napi.network')

            task = {
                'task_id': task_obj.id
            }

            response.append(task)

        return Response(response, status=status.HTTP_202_ACCEPTED)

    @logs_method_apiview
    @raise_json_validate('')
    @permission_classes_apiview((IsAuthenticated, Write))
    @permission_obj_apiview([write_objv6_permission])
    @atomic
    def delete(self, request, *args, **kwargs):
        """Delete Ipv6."""

        response = list()
        obj_ids = kwargs['obj_ids'].split(';')

        user = request.user

        for obj_id in obj_ids:
            task_obj = tasks.delete_ipv6.apply_async(
                args=[obj_id, user.id], queue='napi.network')

            task = {
                'task_id': task_obj.id
            }

            response.append(task)

        return Response(response, status=status.HTTP_202_ACCEPTED)
