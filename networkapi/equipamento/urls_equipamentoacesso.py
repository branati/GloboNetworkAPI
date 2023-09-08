# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.equipamento.resource.EquipAccessEditResource import EquipAccessEditResource
from networkapi.equipamento.resource.EquipAccessGetResource import EquipAccessGetResource
from networkapi.equipamento.resource.EquipAccessListResource import EquipAccessListResource
from networkapi.equipamento.resource.EquipamentoAcessoResource import EquipamentoAcessoResource

equipment_access_get_resource = EquipAccessGetResource()
equipment_access_edit_resource = EquipAccessEditResource()
equipment_access_resource = EquipamentoAcessoResource()
equipment_access_list_resource = EquipAccessListResource()

urlpatterns = [
    re_path(r'^$', equipment_access_resource.handle_request,
        name='equipmentaccess.insert.search'),
    re_path(r'^id/(?P<id_acesso>[^/]+)/$',
        equipment_access_get_resource.handle_request,
        name='equipmentaccess.get.by.id'),
    re_path(r'^(?P<id_equipamento>[^/]+)/(?P<id_tipo_acesso>[^/]+)/$',
        equipment_access_resource.handle_request,
        name='equipmentaccess.update.remove.by.pk'),
    re_path(r'^name/$', equipment_access_list_resource.handle_request,
        name='equipmentaccess.list.by.name'),
    re_path(r'^edit/$', equipment_access_edit_resource.handle_request,
        name='equipmentaccess.edit.by.id'),
]
