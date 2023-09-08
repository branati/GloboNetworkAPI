# -*- coding: utf-8 -*-
# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.api_vrf import views

urlpatterns = [
    # 'networkapi.api_vrf.views',
    re_path(r'^v3/vrf/((?P<vrf_ids>[;\w]+)/)?$',
        views.VrfDBView.as_view()),

]
