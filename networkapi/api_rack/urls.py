# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns, url
from django.urls import re_path
from networkapi.api_rack import views as rack_views
from networkapi.api_rack import facade as rack_facade


from networkapi.api_rack.views import RackDeployView
from networkapi.api_rack.views import RackForeman
from networkapi.api_rack.views import RackView

urlpatterns = [
    re_path(r'^rack/(?P<rack_id>\d+)/equipments/$', rack_views.RackDeployView.as_view()),
    re_path(r'^rack/foreman/(?P<rack_id>\d+)/', rack_views.RackForeman.as_view()),
    re_path(r'^rack/fabric/(?P<fabric_id>\d+)[/]$', rack_views.RackView.as_view()),
    re_path(r'^rack/$', rack_views.RackView.as_view()),
    re_path(r'^rack/(?P<rack_id>\d+)/$', rack_views.RackView.as_view()),
    re_path(r'^rack/config/(?P<rack_id>\d+)/$', rack_views.RackConfigView.as_view()),
    re_path(r'^rack/environmentvlan/(?P<rack_id>\d+)/$', rack_views.RackEnvironmentView.as_view()),
    re_path(r'^rack/list/all/$', rack_views.RackView.as_view()),
    re_path(r'^rack/next/', rack_facade.available_rack_number),

    re_path(r'^dc/(?P<dc_id>\d+)/$', rack_views.DataCenterView.as_view()),
    re_path(r'^dc/$', rack_views.DataCenterView.as_view()),
    re_path(r'^dcrooms/(?P<fabric_id>\d+)/$', rack_views.FabricView.as_view()),
    re_path(r'^dcrooms/$', rack_views.FabricView.as_view()),
    re_path(r'^dcrooms/id/(?P<fabric_id>\d+)/$', rack_views.FabricView.as_view()),
    re_path(r'^dcrooms/name/(?P<fabric_name>\s+)/$', rack_views.FabricView.as_view()),
    re_path(r'^dcrooms/dc/(?P<dc_id>\d+)/$', rack_views.FabricView.as_view()),

]

