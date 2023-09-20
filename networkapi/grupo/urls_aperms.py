# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.grupo.resource.AdministrativePermissionAddResource import AdministrativePermissionAddResource
from networkapi.grupo.resource.AdministrativePermissionAlterRemoveResource import AdministrativePermissionAlterRemoveResource
from networkapi.grupo.resource.AdministrativePermissionByGroupUserResource import AdministrativePermissionByGroupUserResource
from networkapi.grupo.resource.AdministrativePermissionGetAllResource import AdministrativePermissionGetAllResource
from networkapi.grupo.resource.AdministrativePermissionGetByIdResource import AdministrativePermissionGetByIdResource

aperms_get_by_group = AdministrativePermissionByGroupUserResource()
aperms_add_resource = AdministrativePermissionAddResource()
aperms_get_by_pk_resource = AdministrativePermissionGetByIdResource()
aperms_get_all_resource = AdministrativePermissionGetAllResource()
aperms_alter_remove_resource = AdministrativePermissionAlterRemoveResource()

urlpatterns = [
    re_path(r'^$', aperms_add_resource.handle_request,
        name='administrative.permission.add'),
    # re_path(r'^all/$', aperms_get_all_resource.handle_request,
    #     name='administrative.permission.get.all'),
    re_path(r'^(?P<id_perm>[^/]+)/$', aperms_alter_remove_resource.handle_request,
        name='administrative.permission.update.remove.by.pk'),
    re_path(r'^group/(?P<id_ugroup>[^/]+)/$', aperms_get_by_group.handle_request,
        name='administrative.permission.get.by.group'),
    re_path(r'^get/(?P<id_perm>[^/]+)/$', aperms_get_by_pk_resource.handle_request,
        name='administrative.permission.get.by.pk')
]
