# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url
from django.urls import re_path

from networkapi.equipamento.resource.EquipmentEnvironmentDeallocateResource import EquipmentEnvironmentDeallocateResource
from networkapi.equipamento.resource.EquipmentGetAllResource import EquipmentGetAllResource
from networkapi.equipamento.resource.EquipmentGetByGroupEquipmentResource import EquipmentGetByGroupEquipmentResource
from networkapi.equipamento.resource.EquipmentGetIpsByAmbiente import EquipmentGetIpsByAmbiente

equipment_get_all_resource = EquipmentGetAllResource()
equipment_get_by_group_resource = EquipmentGetByGroupEquipmentResource()
equipment_get_ips_resource = EquipmentGetIpsByAmbiente()
equipment_environment_remove = EquipmentEnvironmentDeallocateResource()

urlpatterns = [
    re_path(r'^all/$', equipment_get_all_resource.handle_request,
        name='equipment.get.all'),
    re_path(r'^group/(?P<id_egroup>[^/]+)/$', equipment_get_by_group_resource.handle_request,
        name='equipment.get.by.group'),
    re_path(r'^getipsbyambiente/(?P<equip_name>[^/]+)/(?P<id_ambiente>[^/]+)/$', equipment_get_ips_resource.handle_request,
        name='equipment.get.by.ambiente'),
    re_path(r'^(?P<id_equipment>[^/]+)/environment/(?P<id_environment>[^/]+)/$', equipment_environment_remove.handle_request,
        name='equipmentenvironment.remove')
]
