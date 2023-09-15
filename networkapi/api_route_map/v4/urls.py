# -*- coding: utf-8 -*-
# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.api_route_map.v4 import views

urlpatterns = [
    re_path(r'^route-map-entry/((?P<obj_ids>[;\w]+)/)?$',
        views.RouteMapEntryDBView.as_view()),
    re_path(r'^route-map/((?P<obj_ids>[;\w]+)/)?$',
        views.RouteMapDBView.as_view()),
    re_path(r'^bgp/routemap/((?P<obj_ids>[;\w]+)/)?$',
        views.RouteMapView.as_view()),
]
