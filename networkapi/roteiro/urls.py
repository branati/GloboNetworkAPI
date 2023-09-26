# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import include
# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.roteiro.resource.ScriptAddResource import ScriptAddResource
from networkapi.roteiro.resource.ScriptAlterRemoveResource import ScriptAlterRemoveResource
from networkapi.roteiro.resource.ScriptGetAllResource import ScriptGetAllResource
from networkapi.roteiro.resource.ScriptGetEquipmentResource import ScriptGetEquipmentResource
from networkapi.roteiro.resource.ScriptGetScriptTypeResource import ScriptGetScriptTypeResource

script_add_resource = ScriptAddResource()
script_alter_remove_resource = ScriptAlterRemoveResource()
script_get_all_resource = ScriptGetAllResource()
script_get_script_type_resource = ScriptGetScriptTypeResource()
script_get_equipment_resource = ScriptGetEquipmentResource()

urlpatterns = [
    re_path(r'^all/$', script_get_all_resource.handle_request, name='script.get.all'),
    re_path(r'^get/(?P<id_script>[^/]+)/$',
            script_get_all_resource.handle_request, name='script.get.by.id'),
    re_path(r'^edit/(?P<id_script>[^/]+)/$', script_alter_remove_resource.handle_request,
            name='script.update.remove.by.pk'),
    re_path(r'^(?P<id_script>[^/]+)/$', script_alter_remove_resource.handle_request,
            name='script.update.remove.by.pk'),
    re_path(r'^scripttype/(?P<id_script_type>[^/]+)/$', script_get_script_type_resource.handle_request,
            name='script.get.script_type'),
    re_path(r'^equipment/(?P<id_equipment>[^/]+)/$',
            script_get_equipment_resource.handle_request, name='script.get.equipment'),
    re_path(r'^$', script_add_resource.handle_request, name='script.add')
]
