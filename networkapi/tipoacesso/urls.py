# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.tipoacesso.resource.TipoAcessoResource import TipoAcessoResource

access_type_resource = TipoAcessoResource()

urlpatterns = [
    re_path(r'^$', access_type_resource.handle_request,
        name='access_type.insert.search'),
    re_path(r'^(?P<id_tipo_acesso>[^/]+)/$', access_type_resource.handle_request,
        name='access_type.update.remove.by.pk')
]
