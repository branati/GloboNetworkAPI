# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.grupo.resource.PermissionGetAllResource import PermissionGetAllResource

perms_get_all_resource = PermissionGetAllResource()

urlpatterns = [
    re_path(r'^all/$', perms_get_all_resource.handle_request,
        name='permission.get.all')
]
