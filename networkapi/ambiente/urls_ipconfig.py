# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.ambiente.resource.EnvironmentIpConfigResource import EnvironmentIpConfigResource

env_ip_conf_resource = EnvironmentIpConfigResource()

urlpatterns = [
    re_path(r'^$', env_ip_conf_resource.handle_request,
        name='ipconfig.associate'),
]
