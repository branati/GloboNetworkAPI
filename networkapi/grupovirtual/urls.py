# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.grupovirtual.resource.GrupoVirtualResource import GroupVirtualResource

virtual_group_resource = GroupVirtualResource()

urlpatterns = [
    re_path(r'^$', virtual_group_resource.handle_request,
        name='virtual_group.add.remove'),
]
