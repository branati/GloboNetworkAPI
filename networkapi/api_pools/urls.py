# -*- coding: utf-8 -*-
# from django.conf.urls import patterns
# from django.conf.urls import url
from django.urls import re_path

from networkapi.api_pools.views import v3 as views_v3
from networkapi.api_pools.views import v1
urlpatterns = [
    # 'networkapi.api_pools.views.v1',
    # url(r'^pools/save/$', 'save'),
    # url(r'^pools/save_reals/$', 'save_reals'),
    # url(r'^pools/delete/$', 'delete'),
    # url(r'^pools/remove/$', 'remove'),
    # url(r'^pools/create/$', 'create'),
    # url(r'^pools/enable/$', 'enable'),
    # url(r'^pools/disable/$', 'disable'),

    re_path(r'^pools/$', v1.pool_list),
    re_path(r'^pools/pool_list_by_reqvip/$', v1.pool_list_by_reqvip),
    # re_path(r'^pools/list_healthchecks/$', 'healthcheck_list'),
    re_path(r'^pools/getbypk/(?P<id_server_pool>[^/]+)/$', v1.get_by_pk),
    re_path(r'^pools/get_all_members/(?P<id_server_pool>[^/]+)/$',
        v1.list_all_members_by_pool),
    # re_path(r'^pools/get_equip_by_ip/(?P<id_ip>[^/]+)/$', 'get_equipamento_by_ip'),
    # re_path(r'^pools/get_opcoes_pool_by_ambiente/$', 'get_opcoes_pool_by_ambiente'),
    # re_path(
    #     r'^pools/get_requisicoes_vip_by_pool/(?P<id_server_pool>[^/]+)/$', 'get_requisicoes_vip_by_pool'),
    # re_path(
    #     r'^pools/list/by/environment/(?P<environment_id>[^/]+)/$', 'list_by_environment'),
    # re_path(r'^pools/list/members/(?P<pool_id>[^/]+)/$', 'list_pool_members'),
    re_path(r'^pools/list/by/environment/vip/(?P<environment_vip_id>\d+)/$',
        v1.list_by_environment_vip),
    re_path(r'^pools/list/environment/with/pools/$', v1.list_environments_with_pools),

    # re_path(r'^pools/check/status/by/pool/(?P<pool_id>[^/]+)/$',
    #     'chk_status_poolmembers_by_pool'),
    # re_path(r'^pools/check/status/by/vip/(?P<vip_id>[^/]+)/$',
    #     'chk_status_poolmembers_by_vip'),

    # re_path(r'^pools/management/$', 'management_pools'),

    re_path(r'^pools/options/$', v1.list_all_options),
    # re_path(r'^pools/options/save/$', 'save_pool_option'),
    re_path(r'^pools/options/(?P<option_id>\d+)/$', v1.list_option_by_pk),

    # re_path(r'^pools/environment_options/$', 'list_all_environment_options'),
    # re_path(r'^pools/environment_options/save/$', 'save_environment_options'),
    # re_path(r'^pools/environment_options/(?P<environment_option_id>\d+)/$',
    #     'environment_options_by_pk'),

    re_path(r'^pools/list/environments/environmentvip/$',
        v1.list_environment_environment_vip_related),
    # re_path(r'^pools/getipsbyambiente/(?P<equip_name>[^/]+)/(?P<id_ambiente>[^/]+)/$',
    #     'get_available_ips_to_add_server_pool'),


    ########################
    # Manage Pool V3
    ########################
    re_path(r'^v3/pool/deploy/async/(?P<obj_ids>[;\w]+)/$',
        views_v3.PoolAsyncDeployView.as_view()),
    re_path(r'^v3/pool/deploy/(?P<obj_ids>[;\w]+)/member/status/$',
        views_v3.PoolMemberStateView.as_view()),
    re_path(r'^v3/pool/deploy/(?P<obj_ids>[;\w]+)/$',
        views_v3.PoolDeployView.as_view()),
    re_path(r'^v3/pool/details/((?P<obj_ids>[;\w]+)/)?$',
        views_v3.PoolDBDetailsView.as_view()),
    re_path(r'^v3/pool/((?P<obj_ids>[;\w]+)/)?$', views_v3.PoolDBView.as_view()),
    re_path(r'^v3/pool/environment-vip/(?P<environment_vip_id>[^/]+)/$',
        views_v3.PoolEnvironmentVip.as_view()),

    re_path(r'^v3/option-pool/environment/(?P<environment_id>\d+)/$',
        views_v3.OptionPoolEnvironmentView.as_view()),

    # url(r'^v3/option-pool/((?P<obj_ids>[;\w]+)/)?$',
    #     views_v3.OptionPoolView.as_view()),
]
