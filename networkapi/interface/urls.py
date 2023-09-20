# -*- coding: utf-8 -*-
from __future__ import absolute_import

#from django.conf.urls import patterns
#from django.conf.urls import url

from django.urls import re_path

from networkapi.interface.resource.InterfaceDisconnectResource import InterfaceDisconnectResource
from networkapi.interface.resource.InterfaceGetResource import InterfaceGetResource
from networkapi.interface.resource.InterfaceResource import InterfaceResource

interface_resource = InterfaceResource()
interface_get_resource = InterfaceGetResource()
interface_disconnect_resource = InterfaceDisconnectResource()

urlpatterns = [
    re_path(r'^$', interface_resource.handle_request,
        name='interface.insert'),
    re_path(r'^(?P<id_interface>[^/]+)/$', interface_resource.handle_request,
        name='interface.update.remove.by.pk'),
    re_path(r'^(?P<id_interface>[^/]+)/get/$', interface_get_resource.handle_request,
        name='interface.get.by.pk'),
    re_path(r'^get/(?P<channel_name>[^/]+)/(?P<id_equipamento>[^/]+)[/]?$', interface_get_resource.handle_request,
        name='interface.list.by.equip'),
    re_path(r'^get-by-channel/(?P<channel_name>[^/]+)/(?P<equip_name>[^/]+)[/]/?$', interface_get_resource.handle_request,
        name='interface.get.by.pk'),
    re_path(r'^equipamento/(?P<id_equipamento>[^/]+)/$', interface_resource.handle_request,
        name='interface.search.by.equipment'),
    re_path(r'^equipment/(?P<id_equipamento>[^/]+)/$', interface_resource.handle_request, {'new': True},
        name='interface.search.by.equipment.new'),
    re_path(r'^(?P<id_interface>[^/]+)/(?P<back_or_front>[^/]+)/$', interface_disconnect_resource.handle_request,
        name='interface.remove.connection'),
    re_path(r'^(?P<nome_interface>.+?)/equipamento/(?P<id_equipamento>[^/]+)/$', interface_resource.handle_request,
        name='interface.search.by.interface.equipment'),
    re_path(r'^(?P<nome_interface>.+?)/equipment/(?P<id_equipamento>[^/]+)/$', interface_resource.handle_request, {'new': True},
        name='interface.search.by.interface.equipment.new')
]
