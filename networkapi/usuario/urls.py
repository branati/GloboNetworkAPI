# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.usuario.resource.UsuarioGetResource import UsuarioGetResource

user_get_resource = UsuarioGetResource()

urlpatterns = [
    re_path(r'^get/$', user_get_resource.handle_request,
        name='user.list.with.group')
]
