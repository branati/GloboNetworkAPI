# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.equipamento.resource.EquipmentTypeAddResource import EquipmentTypeAddResource
from networkapi.equipamento.resource.EquipmentTypeGetAllResource import EquipmentTypeGetAllResource

equipment_type_get_all_resource = EquipmentTypeGetAllResource()
equipment_type_add_resource = EquipmentTypeAddResource()


urlpatterns = [
    re_path(r'^all/$', equipment_type_get_all_resource.handle_request,
        name='equipment_type.get.all'),
    re_path(r'^$', equipment_type_add_resource.handle_request,
        name='equipment_type.add'),
]
