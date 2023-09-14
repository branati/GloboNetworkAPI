# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
from django.conf.urls import include
# from django.conf.urls import url
from django.urls import re_path

from networkapi.api_equipment.views import v1
from networkapi.api_equipment.views import v3


urlpatterns = [
    re_path(r'^equipment/get_routers_by_environment/(?P<env_id>\d+)/$',
        v1.EquipmentRoutersView.as_view()),
    re_path(r'^v3/equipment/((?P<obj_id>[;\w]+)/)?$', v3.EquipmentView.as_view()),
    re_path(r'^v4/', include('networkapi.api_equipment.v4.urls')),

]
