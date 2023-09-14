# -*- coding: utf-8 -*-
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView

from networkapi.api_equipment import facade
from networkapi.api_rest import exceptions as api_exceptions
from networkapi.equipamento.models import Equipamento
from networkapi.util.geral import CustomResponse
# from django.db.transaction import atomic


log = logging.getLogger(__name__)


class EquipmentRoutersView(APIView):

    def get(self, request, *args, **kwargs):
        try:

            env_id = kwargs.get('env_id')

            data = dict()

            if env_id:
                log.info('Get Routers by environment.')

                routers_list = []
                rot_do_ambiente = facade.get_routers_by_environment(
                    int(env_id))
                for r in rot_do_ambiente:
                    router_id = r.equipamento.id
                    router = Equipamento().get_by_pk(router_id)
                    routers_list.append(facade.get_equipment_map(router))

                data['routers'] = routers_list

            return CustomResponse(data, status=status.HTTP_200_OK, request=request)

        except ObjectDoesNotExist as exception:
            log.error(exception)
            raise api_exceptions.ObjectDoesNotExistException(
                'Equipment Does Not Exist')

        except Exception as exception:
            log.exception(exception)
            raise api_exceptions.NetworkAPIException()
