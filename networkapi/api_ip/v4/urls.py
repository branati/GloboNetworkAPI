# -*- coding: utf-8 -*-
# from django.conf.urls import patterns
from django.conf.urls import include
# from django.conf.urls import url

from django.urls import re_path

from networkapi.api_ip.v4 import views

urlpatterns = [
    re_path(r'^ipv4/async/((?P<obj_ids>[;\w]+)/)?$',
        views.IPv4V4AsyncView.as_view()),
    re_path(r'^ipv6/async/((?P<obj_ids>[;\w]+)/)?$',
        views.IPv6V4AsyncView.as_view()),
    re_path(r'^ipv4/((?P<obj_ids>[;\w]+)/)?$', views.IPv4V4View.as_view()),
    re_path(r'^ipv6/((?P<obj_ids>[;\w]+)/)?$', views.IPv6V4View.as_view()),
    re_path(r'^ipv6/((?P<obj_ids>[;\w]+)/)?$', views.IPv6V4View.as_view()),

]
