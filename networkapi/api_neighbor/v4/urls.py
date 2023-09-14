# -*- coding: utf-8 -*-
# from django.conf.urls import patterns
# from django.conf.urls import url
from django.urls import re_path
from networkapi.api_neighbor.v4 import views

urlpatterns = [
    re_path(r'^neighborv4/deploy/((?P<obj_ids>[;\w]+)/)?$',
        views.NeighborV4DeployView.as_view()),
    re_path(r'^neighborv4/((?P<obj_ids>[;\w]+)/)?$',
        views.NeighborV4DBView.as_view()),
    re_path(r'^neighborv6/deploy/((?P<obj_ids>[;\w]+)/)?$',
        views.NeighborV6DeployView.as_view()),
    re_path(r'^neighborv6/((?P<obj_ids>[;\w]+)/)?$',
        views.NeighborV6DBView.as_view()),
    re_path(r'^bgp/neighborv4/((?P<obj_ids>[;\w]+)/)?$',
        views.NeighborDBView.as_view())
]
