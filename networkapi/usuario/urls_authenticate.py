# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.usuario.resource.AuthenticateResource import AuthenticateResource

authenticate_resource = AuthenticateResource()

urlpatterns = [
    re_path(r'^$', authenticate_resource.handle_request,
        name='user.authenticate'),
]
