# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.ambiente.resource.EnvironmentVipResource import EnvironmentVipResource
from networkapi.ambiente.resource.EnvironmentVipSearchResource import EnvironmentVipSearchResource
from networkapi.ambiente.resource.RequestAllVipsEnviromentVipResource import RequestAllVipsEnviromentVipResource

environment_vip_resource = EnvironmentVipResource()
environment_vip_search_resource = EnvironmentVipSearchResource()
environment_vip_search_all_vips_resource = RequestAllVipsEnviromentVipResource()

urlpatterns = [
    re_path(r'^$', environment_vip_resource.handle_request,
        name='environment.vip.add'),
    re_path(r'^all/', environment_vip_resource.handle_request,
        name='environment.vip.all'),
    re_path(r'^search/$', environment_vip_search_resource.handle_request,
        name='environment.vip.search'),
    re_path(r'^search/(?P<id_vlan>[^/]+)/$', environment_vip_search_resource.handle_request,
        name='environment.vip.search'),
    re_path(r'^(?P<id_environment_vip>[^/]+)/$', environment_vip_resource.handle_request,
        name='environment.vip.update.remove'),
    re_path(r'^(?P<id_environment_vip>[^/]+)/vip/all/$', environment_vip_search_all_vips_resource.handle_request,
        name='environmentvip.vips.all')
]
