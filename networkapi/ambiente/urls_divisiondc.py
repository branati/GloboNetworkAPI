# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.ambiente.resource.DivisionDcAddResource import DivisionDcAddResource
from networkapi.ambiente.resource.DivisionDcAlterRemoveResource import DivisionDcAlterRemoveResource
from networkapi.ambiente.resource.DivisionDcGetAllResource import DivisionDcGetAllResource

division_dc_add_resource = DivisionDcAddResource()
division_dc_alter_remove_resource = DivisionDcAlterRemoveResource()
division_dc_get_all_resource = DivisionDcGetAllResource()

urlpatterns = [
    re_path(r'^$', division_dc_add_resource.handle_request,
        name='division_dc.add'),
    re_path(r'^all/$', division_dc_get_all_resource.handle_request,
        name='division_dc.get.all'),
    re_path(r'^(?P<id_divisiondc>[^/]+)/$', division_dc_alter_remove_resource.handle_request,
        name='division_dc.update.remove.by.pk'),
]
