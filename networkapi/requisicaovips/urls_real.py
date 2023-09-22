# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.requisicaovips.resource.RequestVipsRealResource import RequestVipsRealResource

vip_real = RequestVipsRealResource()

urlpatterns = [
    re_path(r'^equip/(?P<id_equip>\d+)/vip/(?P<id_vip>\d+)/ip/(?P<id_ip>\d+)/$', vip_real.handle_request,
        name='vip.real.add.remove'),
    re_path(r'^(?P<status>enable|disable|check)/equip/(?P<id_equip>\d+)/vip/(?P<id_vip>\d+)/ip/(?P<id_ip>\d+)/$', vip_real.handle_request,
        name='vip.real.enable.disable')
]
