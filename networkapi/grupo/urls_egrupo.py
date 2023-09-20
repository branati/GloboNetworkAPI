# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.grupo.resource.GrupoEquipamentoGetByEquipResource import GrupoEquipamentoGetByEquipResource
from networkapi.grupo.resource.GrupoEquipamentoRemoveAssociationEquipResource import GrupoEquipamentoRemoveAssociationEquipResource
from networkapi.grupo.resource.GrupoResource import GrupoEquipamentoResource

egroup_resource = GrupoEquipamentoResource()
egroup_remove_association_equip_resource = GrupoEquipamentoRemoveAssociationEquipResource()
egroup_get_by_equip_resource = GrupoEquipamentoGetByEquipResource()

urlpatterns = [
    re_path(r'equipamento/(?P<id_equipamento>[^/]+)/egrupo/(?P<id_egrupo>[^/]+)/$', egroup_remove_association_equip_resource.handle_request,
        name='egroup.remove.equip.association'),
    re_path(r'equip/(?P<id_equip>[^/]+)/$', egroup_get_by_equip_resource.handle_request,
        name='egroup.get.by.equip'),
    re_path(r'(?P<id_grupo>[^/]+)/$', egroup_resource.handle_request,
        name='egroup.update.remove.by.pk'),
    re_path(r'$', egroup_resource.handle_request,
        name='egroup.search.insert')
]
