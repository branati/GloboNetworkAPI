# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import include
# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.ip.resource.IPv4AddResource import IPv4AddResource
from networkapi.ip.resource.Ipv4AssocEquipResource import Ipv4AssocEquipResource
from networkapi.ip.resource.IPv4SaveResource import IPv4SaveResource

ipv4_add_resource = IPv4AddResource()
ipv4_save_resource = IPv4SaveResource()
ipv4_assoc_equip_resource = Ipv4AssocEquipResource()

urlpatterns = [
    re_path(r'^$', ipv4_add_resource.handle_request,
        name='ipv4.insert'),
    re_path(r'^save/$',
        ipv4_save_resource.handle_request, name='ipv4.save'),
    re_path(r'^assoc/$', ipv4_assoc_equip_resource.handle_request,
        name='ipv4.assoc.equip'),
]
