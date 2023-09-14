# -*- coding: utf-8 -*-
# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.api_network.views import v3
from networkapi.api_network.views.v1 import DHCPRelayIPv4ByPkView
from networkapi.api_network.views.v1 import DHCPRelayIPv4View
from networkapi.api_network.views.v1 import DHCPRelayIPv6ByPkView
from networkapi.api_network.views.v1 import DHCPRelayIPv6View
from networkapi.api_network.views.v1 import networksIPv4_by_pk
from networkapi.api_network.views.v1 import networksIPv6_by_pk
from networkapi.api_network.views.v1 import networkIPv4_deploy
from networkapi.api_network.views.v1 import networkIPv6_deploy
urlpatterns = [
    # 'networkapi.api_network.views.v1',
    re_path(r'^networkv4/$', v3.NetworkIPv4View.as_view()),
    re_path(r'^networkv6/$', v3.NetworkIPv6View.as_view()),
    re_path(r'^networkv4/(?P<network_id>\d+)/$', networksIPv4_by_pk),
    re_path(r'^networkv6/(?P<network_id>\d+)/$', networksIPv6_by_pk),
    re_path(r'^networkv4/(?P<network_id>\d+)/equipments/$', networkIPv4_deploy),
    re_path(r'^networkv6/(?P<network_id>\d+)/equipments/$', networkIPv6_deploy),
    re_path(r'^dhcprelayv4/$', DHCPRelayIPv4View.as_view()),
    re_path(r'^dhcprelayv6/$', DHCPRelayIPv6View.as_view()),
    re_path(r'^dhcprelayv4/(?P<dhcprelay_id>\d+)/$',
        DHCPRelayIPv4ByPkView.as_view()),
    re_path(r'^dhcprelayv6/(?P<dhcprelay_id>\d+)/$',
        DHCPRelayIPv6ByPkView.as_view()),

    ########################
    # Network V3
    ########################
    re_path(r'^v3/networkv4/deploy/async/((?P<obj_ids>[;\w]+)/)?$',
        v3.Networkv4DeployAsyncView.as_view()),
    re_path(r'^v3/networkv6/deploy/async/((?P<obj_ids>[;\w]+)/)?$',
        v3.Networkv6DeployAsyncView.as_view()),
    re_path(r'^v3/networkv4/async/((?P<obj_ids>[;\w]+)/)?$',
        v3.Networkv4AsyncView.as_view()),
    re_path(r'^v3/networkv6/async/((?P<obj_ids>[;\w]+)/)?$',
        v3.Networkv6AsyncView.as_view()),
    re_path(r'^v3/networkv4/force/((?P<obj_ids>[;\w]+)/)?$',
        v3.NetworkIPv4ForceView.as_view()),
    re_path(r'^v3/networkv6/force/((?P<obj_ids>[;\w]+)/)?$',
        v3.NetworkIPv6ForceView.as_view()),
    re_path(r'^v3/networkv4/deploy/((?P<obj_ids>[;\w]+)/)?$',
        v3.NetworkIPv4DeployView.as_view()),
    re_path(r'^v3/networkv6/deploy/((?P<obj_ids>[;\w]+)/)?$',
        v3.NetworkIPv6DeployView.as_view()),
    re_path(r'^v3/networkv4/((?P<obj_ids>[;\w]+)/)?$',
        v3.NetworkIPv4View.as_view()),
    re_path(r'^v3/networkv6/((?P<obj_ids>[;\w]+)/)?$',
        v3.NetworkIPv6View.as_view()),

]
