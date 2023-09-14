# -*- coding: utf-8 -*-


from django.conf.urls import include

# from django.conf.urls import patterns
#from django.conf.urls import url

from django.urls import re_path

from networkapi.api_ip import views

urlpatterns = [
    re_path(r'^v3/ipv4/async/((?P<obj_ids>[;\w]+)/)?$',
        views.IPv4AsyncView.as_view()),
    re_path(r'^v3/ipv6/async/((?P<obj_ids>[;\w]+)/)?$',
        views.IPv6AsyncView.as_view()),
    re_path(r'^v3/ipv4/((?P<obj_ids>[;\w]+)/)?$', views.IPv4View.as_view()),
    re_path(r'^v3/ipv6/((?P<obj_ids>[;\w]+)/)?$', views.IPv6View.as_view()),
    re_path(r'^v3/ipv6/((?P<obj_ids>[;\w]+)/)?$', views.IPv6View.as_view()),
    re_path(r'^v4/', include('networkapi.api_ip.v4.urls')),

]
