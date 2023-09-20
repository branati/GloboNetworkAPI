# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.interface.resource.InterfaceTypeGetAllResource import InterfaceTypeGetAllResource

interface_type_get_all_resource = InterfaceTypeGetAllResource()

urlpatterns = [
    re_path(r'^get-type[/]?$', interface_type_get_all_resource.handle_request,
        name='interfacetype.get'),
]
