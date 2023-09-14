# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url
from django.urls import re_path
from networkapi.api_equipment.v4.views import EquipmentV4View


urlpatterns = [
    re_path(r'^equipment/((?P<obj_id>[;\w]+)/)?$', EquipmentV4View.as_view())

]
