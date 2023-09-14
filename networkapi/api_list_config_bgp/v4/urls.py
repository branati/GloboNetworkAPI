# -*- coding: utf-8 -*-
# from django.conf.urls import patterns
# from django.conf.urls import url
from django.urls import re_path

from networkapi.api_list_config_bgp.v4 import views

urlpatterns = [
    re_path(r'^list-config-bgp/((?P<obj_ids>[;\w]+)/)?$',
        views.ListConfigBGPDBView.as_view()),
]
