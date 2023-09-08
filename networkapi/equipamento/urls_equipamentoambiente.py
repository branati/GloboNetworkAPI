# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.equipamento.resource.EquipamentoResource import EquipamentoAmbienteResource

equipment_environment_resource = EquipamentoAmbienteResource()

urlpatterns = [
    re_path(r'^$', equipment_environment_resource.handle_request,
        name='equipmentenvironment.insert'),
    re_path(r'^update/$', equipment_environment_resource.handle_request,
        name='equipmentenvironment.update')
]
