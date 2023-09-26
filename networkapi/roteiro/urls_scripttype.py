# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import include
# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.roteiro.resource.ScriptTypeAddResource import ScriptTypeAddResource
from networkapi.roteiro.resource.ScriptTypeAlterRemoveResource import ScriptTypeAlterRemoveResource
from networkapi.roteiro.resource.ScriptTypeGetAllResource import ScriptTypeGetAllResource

script_type_add_resource = ScriptTypeAddResource()
script_type_alter_remove_resource = ScriptTypeAlterRemoveResource()
script_type_get_all_resource = ScriptTypeGetAllResource()

urlpatterns = [
    re_path(r'^$', script_type_add_resource.handle_request,
            name='script_type.add'),
    re_path(r'^all/$', script_type_get_all_resource.handle_request,
            name='script_type.get.all'),
    re_path(r'^(?P<id_script_type>[^/]+)/$', script_type_alter_remove_resource.handle_request,
            name='script_type.update.remove.by.pk')
]
