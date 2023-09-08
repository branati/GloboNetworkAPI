# -*- coding: utf-8 -*-
from django.conf.urls import include
# from django.conf.urls import patterns
# from django.conf.urls import url
from django.urls import re_path
urlpatterns = [
    re_path(r'^v4/', include('networkapi.api_asn.v4.urls')),

]
