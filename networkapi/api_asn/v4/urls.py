# -*- coding: utf-8 -*-
#from django.conf.urls import patterns
#from django.conf.urls import url
from django.urls import re_path
from networkapi.api_asn.v4 import views

urlpatterns = [
    re_path(r'^asnequipment/asn/((?P<asn_ids>[;\w]+)/)?$',
        views.AsEquipmentDBView.as_view()),
    re_path(r'^asnequipment/equipment/((?P<equip_ids>[;\w]+)/)?$',
        views.AsEquipmentDBView.as_view()),
    re_path(r'^asnequipment/((?P<obj_ids>[;\w]+)/)?$',
        views.AsEquipmentDBView.as_view()),
    re_path(r'^as/((?P<obj_ids>[;\w]+)/)?$',
        views.AsDBView.as_view())
]
