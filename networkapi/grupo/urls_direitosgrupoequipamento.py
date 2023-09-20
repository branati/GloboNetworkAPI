# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.grupo.resource.GrupoResource import DireitoGrupoEquipamentoResource

access_right_resource = DireitoGrupoEquipamentoResource()

urlpatterns = [
    re_path(r'^$', access_right_resource.handle_request,
        name='access_right.search.insert'),
    # re_path(r'^ugrupo/(?P<id_grupo_usuario>[^/]+)/$', access_right_resource.handle_request,
    #     name='access_right.search.by.ugroup'),
    re_path(r'^egrupo/(?P<id_grupo_equipamento>[^/]+)/$', access_right_resource.handle_request,
        name='access_right.search.by.egroup'),
    re_path(r'^(?P<id_direito>[^/]+)/$', access_right_resource.handle_request,
        name='access_right.search.update.remove.by.pk'),
]
