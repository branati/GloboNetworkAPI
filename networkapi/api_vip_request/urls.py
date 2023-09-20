# -*- coding: utf-8 -*-
# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.api_vip_request.views import v3 as views
from networkapi.api_vip_request.views import v1 as views_v1


urlpatterns = [
    # 'networkapi.api_vip_request.views.v1',
    # url(r'^vip/request/save/?(?P<pk>\d+)?/?$', 'save'),
    # url(r'^vip/request/add/pools/$', 'add_pools'),
    # url(r'^vip/request/delete/(?P<delete_pools>\d+)/$', 'delete'),
    re_path(r'^vip/list/environment/by/environment/vip/(?P<environment_vip_id>\d+)/$',
        views_v1.list_environment_by_environment_vip),
    re_path(r'^vip/request/get/(?P<pk>\d+)/$', views_v1.get_by_pk),


    ########################
    # Vip Resquest V3
    ########################

    re_path(r'^v3/vip-request/details/((?P<obj_ids>[;\w]+)/)?$',
        views.VipRequestDBDetailsView.as_view()),
    re_path(r'^v3/vip-request/deploy/async/((?P<obj_ids>[;\w]+)/)?$',
        views.VipRequestAsyncDeployView.as_view()),
    re_path(r'^v3/vip-request/deploy/((?P<obj_ids>[;\w]+)/)?$',
        views.VipRequestDeployView.as_view()),
    re_path(r'^v3/vip-request/((?P<obj_ids>[;\w]+)/)?$',
        views.VipRequestDBView.as_view()),
    re_path(r'^v3/vip-request/pool/(?P<pool_id>[^/]+)/$',
        views.VipRequestPoolView.as_view()),  # GET
]
