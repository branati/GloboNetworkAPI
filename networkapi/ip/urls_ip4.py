# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import include
# from django.conf.urls import patterns
# from django.conf.urls import url
from django.urls import re_path

from networkapi.ip.resource.IPv4DeleteResource import IPv4DeleteResource
from networkapi.ip.resource.IPv4EditResource import IPv4EditResource

ipv4_delete_resource = IPv4DeleteResource()
ipv4_edit_resource = IPv4EditResource()

urlpatterns = [
    re_path(r'^delete/(?P<id_ipv4>[^/]+)', ipv4_delete_resource.handle_request,
        name='ip4.delete'),
    re_path(r'^edit', ipv4_edit_resource.handle_request,
        name='ip4.edit'),
]
