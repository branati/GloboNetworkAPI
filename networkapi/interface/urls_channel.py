# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.interface.resource.InterfaceChannelResource import InterfaceChannelResource

interface_channel_resource = InterfaceChannelResource()

urlpatterns = [
    re_path(r'^editar[/]?$', interface_channel_resource.handle_request,
        name='channel.edit'),
    re_path(r'^inserir[/]?$', interface_channel_resource.handle_request,
        name='channel.add'),
    re_path(r'^delete/(?P<channel_name>[^/]+)/$', interface_channel_resource.handle_request,
        name='channel.delete'),
    # url(r'^get-by-name[/]?$', interface_channel_resource.handle_request,
    #     name='channel.get')
]
