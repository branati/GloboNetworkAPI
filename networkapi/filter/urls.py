# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.filter.resource.FilterAddResource import FilterAddResource
from networkapi.filter.resource.FilterAlterRemoveResource import FilterAlterRemoveResource
from networkapi.filter.resource.FilterAssociateResource import FilterAssociateResource
from networkapi.filter.resource.FilterDissociateOneResource import FilterDissociateOneResource
from networkapi.filter.resource.FilterGetByIdResource import FilterGetByIdResource
from networkapi.filter.resource.FilterListAllResource import FilterListAllResource

filter_list_all = FilterListAllResource()
filter_add = FilterAddResource()
filter_alter_remove = FilterAlterRemoveResource()
filter_get_by_id = FilterGetByIdResource()
filter_associate = FilterAssociateResource()
filter_dissociate_one = FilterDissociateOneResource()

urlpatterns = [
    re_path(r'^all/$', filter_list_all.handle_request,
        name='filter.list.all'),
    re_path(r'^$', filter_add.handle_request,
        name='filter.add'),
    re_path(r'^(?P<id_filter>[^/]+)/$', filter_alter_remove.handle_request,
        name='filter.alter.remove'),
    re_path(r'^get/(?P<id_filter>[^/]+)/$', filter_get_by_id.handle_request,
        name='filter.get.by.id'),
    re_path(r'^(?P<id_filter>[^/]+)/equiptype/(?P<id_equiptype>[^/]+)/$', filter_associate.handle_request,
        name='filter.associate'),
    re_path(r'^(?P<id_filter>[^/]+)/dissociate/(?P<id_equip_type>[^/]+)/$', filter_dissociate_one.handle_request,
        name='filter.dissociate.one')
]
