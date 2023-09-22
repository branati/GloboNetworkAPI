# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.requisicaovips.resource.OptionVipAllGetByEnvironmentVipResource import OptionVipAllGetByEnvironmentVipResource
from networkapi.requisicaovips.resource.OptionVipAllResource import OptionVipAllResource
from networkapi.requisicaovips.resource.OptionVipEnvironmentVipAssociationResource import OptionVipEnvironmentVipAssociationResource
from networkapi.requisicaovips.resource.OptionVipGetTrafficReturnByNameResource import OptionVipGetTrafficReturnByNameResource
from networkapi.requisicaovips.resource.OptionVipResource import OptionVipResource

option_vip = OptionVipResource()
option_vip_environment_vip_association = OptionVipEnvironmentVipAssociationResource()
option_vip_all = OptionVipAllResource()
option_vip_environment_vip = OptionVipAllGetByEnvironmentVipResource()
trafficreturn_search = OptionVipGetTrafficReturnByNameResource()

urlpatterns = [
    re_path(r'^all/$', option_vip_all.handle_request,
        name='option.vip.all'),
    re_path(r'^$', option_vip.handle_request,
        name='option.vip.add'),
    re_path(r'^(?P<id_option_vip>[^/]+)/$', option_vip.handle_request,
        name='option.vip.update.remove.search'),
    re_path(r'^(?P<id_option_vip>[^/]+)/environmentvip/(?P<id_environment_vip>[^/]+)/$', option_vip_environment_vip_association.handle_request,
        name='option.vip.environment.vip.associate.disassociate'),
    re_path(r'^environmentvip/(?P<id_environment_vip>[^/]+)/$', option_vip_environment_vip.handle_request,
        name='option.vip.by.environment.vip'),
    re_path(r'^trafficreturn/search/$', trafficreturn_search.handle_request,
        name='option.vip.trafficreturn'),
]
