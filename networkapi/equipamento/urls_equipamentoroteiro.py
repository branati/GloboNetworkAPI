# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.equipamento.resource.EquipScriptListResource import EquipScriptListResource

equipment_script_list_resource = EquipScriptListResource()

urlpatterns = [
    re_path(r'^name/$', equipment_script_list_resource.handle_request,
        name='equipmentscript.list.by.name'),
]
