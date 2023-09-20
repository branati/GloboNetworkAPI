# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.grupo.resource.GroupUserAddResource import GroupUserAddResource
from networkapi.grupo.resource.GroupUserAlterRemoveResource import GroupUserAlterRemoveResource
from networkapi.grupo.resource.GroupUserGetAllResource import GroupUserGetAllResource
from networkapi.grupo.resource.GroupUserGetByIdResource import GroupUserGetByIdResource

ugroup_get_all_resource = GroupUserGetAllResource()
ugroup_get_by_id_resource = GroupUserGetByIdResource()
ugroup_alter_remove_resource = GroupUserAlterRemoveResource()
ugroup_add_resource = GroupUserAddResource()

urlpatterns = [
    re_path(r'^all/$', ugroup_get_all_resource.handle_request,
        name='ugroup.get.all'),
    re_path(r'^get/(?P<id_ugroup>[^/]+)/$', ugroup_get_by_id_resource.handle_request,
        name='ugroup.get'),
    re_path(r'^$', ugroup_add_resource.handle_request,
        name='ugroup.add'),
    re_path(r'^(?P<id_ugroup>[^/]+)/$', ugroup_alter_remove_resource.handle_request,
        name='ugroup.alter.remove')
]
