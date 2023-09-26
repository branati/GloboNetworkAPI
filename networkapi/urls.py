# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include
# from django.conf.urls import patterns
# from django.conf.urls import url
from django.urls import re_path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse

from networkapi.check.CheckAction import CheckAction
# from django.conf.urls.defaults import *


api_prefix = r'^api/'

urlpatterns = [
    # new API URL patterns are all prefixed with '/api/'
    re_path(api_prefix, include('networkapi.api_asn.urls')),
    re_path(api_prefix, include('networkapi.api_aws.urls')),
    re_path(api_prefix, include('networkapi.api_deploy.urls')),
    re_path(api_prefix, include('networkapi.api_environment.urls')),
    re_path(api_prefix, include('networkapi.api_environment_vip.urls')),
    re_path(api_prefix, include('networkapi.api_equipment.urls')),
    # re_path(api_prefix, include('networkapi.api_healthcheck.urls')),
    re_path(api_prefix, include('networkapi.api_interface.urls')),
    re_path(api_prefix, include('networkapi.api_channel.urls')),
    re_path(api_prefix, include('networkapi.api_ip.urls')),
    re_path(api_prefix, include('networkapi.api_list_config_bgp.urls')),
    re_path(api_prefix, include('networkapi.api_neighbor.urls')),
    re_path(api_prefix, include('networkapi.api_network.urls')),
    re_path(api_prefix, include('networkapi.api_ogp.urls')),
    re_path(api_prefix, include('networkapi.api_peer_group.urls')),
    re_path(api_prefix, include('networkapi.api_pools.urls')),
    re_path(api_prefix, include('networkapi.api_rack.urls')),
    re_path(api_prefix, include('networkapi.api_rest.urls')),
    re_path(api_prefix, include('networkapi.api_route_map.urls')),
    re_path(api_prefix, include('networkapi.api_task.urls')),
    re_path(api_prefix, include('networkapi.api_vip_request.urls')),
    re_path(api_prefix, include('networkapi.api_vlan.urls')),
    re_path(api_prefix, include('networkapi.api_vrf.urls')),
    re_path(api_prefix, include('networkapi.api_vrf.urls')),

    # re_path(api_prefix, include('networkapi.snippets.urls')),
    re_path(api_prefix, include('networkapi.system.urls')),

    # app healthchecks
    re_path(r'^check$', CheckAction().check, name='check'),
    re_path(r'^healthcheck$', lambda _: HttpResponse('WORKING')),

    # equipamento
    re_path(r'^equipamento/', include('networkapi.equipamento.urls')),
    re_path(r'^equipment/', include('networkapi.equipamento.urls_equipment')),
    re_path(r'^equipamentoacesso/',
        include('networkapi.equipamento.urls_equipamentoacesso')),
    re_path(r'^equipamentogrupo/', include('networkapi.equipamento.urls_equipamentogrupo')),
    re_path(r'^equipmenttype/', include('networkapi.equipamento.urls_equipmenttype')),
    re_path(r'^equipamentoambiente/',
        include('networkapi.equipamento.urls_equipamentoambiente')),
    re_path(r'^equipmentscript/', include('networkapi.equipamento.urls_equipmentscript')),
    re_path(r'^equipamentoroteiro/',
        include('networkapi.equipamento.urls_equipamentoroteiro')),
    re_path(r'^brand/', include('networkapi.equipamento.urls_brand')),
    re_path(r'^model/', include('networkapi.equipamento.urls_model')),

    # ambiente
    re_path(r'^ambiente/', include('networkapi.ambiente.urls')),
    re_path(r'^environment/', include('networkapi.ambiente.urls_environment')),
    re_path(r'^divisiondc/', include('networkapi.ambiente.urls_divisiondc')),
    re_path(r'^groupl3/', include('networkapi.ambiente.urls_groupl3')),
    re_path(r'^logicalenvironment/',
        include('networkapi.ambiente.urls_logicalenvironment')),
    re_path(r'^ipconfig/', include('networkapi.ambiente.urls_ipconfig')),

    # rules
    re_path(r'^rule/', include('networkapi.blockrules.urls')),

    # vlan
    re_path(r'^vlan/', include('networkapi.vlan.urls')),
    re_path(r'^net_type/', include('networkapi.vlan.urls_net_type')),

    # ip
    re_path(r'^ip/', include('networkapi.ip.urls')),
    re_path(r'^ipv4/', include('networkapi.ip.urls_ipv4')),
    re_path(r'^ipv6/', include('networkapi.ip.urls_ipv6')),
    re_path(r'^network/', include('networkapi.ip.urls_network')),
    re_path(r'^ip4/', include('networkapi.ip.urls_ip4')),

    # scripts
    re_path(r'^script/', include('networkapi.roteiro.urls')),
    re_path(r'^scripttype/', include('networkapi.roteiro.urls_scripttype')),

    # healthcheckexpect
    re_path(r'^healthcheckexpect/', include('networkapi.healthcheckexpect.urls')),

    # vips
    re_path(r'^vip/', include('networkapi.requisicaovips.urls')),
    re_path(r'^requestvip/', include('networkapi.requisicaovips.urls_requestvip')),
    re_path(r'^real/', include('networkapi.requisicaovips.urls_real')),
    re_path(r'^environment-vip/', include('networkapi.requisicaovips.urls_environment-vip')),
    re_path(r'^environmentvip/', include('networkapi.requisicaovips.urls_environmentvip')),
    re_path(r'^optionvip/', include('networkapi.requisicaovips.urls_optionvip')),

    # grupovirtual
    re_path(r'^grupovirtual/', include('networkapi.grupovirtual.urls')),

    # interface
    re_path(r'^interface/', include('networkapi.interface.urls')),
    re_path(r'^int/', include('networkapi.interface.urls_int')),
    re_path(r'^interfacetype/', include('networkapi.interface.urls_interfacetype')),
    re_path(r'^channel/', include('networkapi.interface.urls_channel')),

    # usuario
    re_path(r'^usuario/', include('networkapi.usuario.urls')),
    re_path(r'^user/', include('networkapi.usuario.urls_user')),
    re_path(r'^authenticate/', include('networkapi.usuario.urls_authenticate')),
    re_path(r'^user-change-pass/', include('networkapi.usuario.urls_user-change-pass')),
    re_path(r'^usergroup/', include('networkapi.usuario.urls_usergroup')),

    # tipoacesso
    re_path(r'^tipoacesso/', include('networkapi.tipoacesso.urls')),

    # grupos
    re_path(r'^ugroup/', include('networkapi.grupo.urls')),
    re_path(r'^egroup/', include('networkapi.grupo.urls_egroup')),
    re_path(r'^egrupo/', include('networkapi.grupo.urls_egrupo')),
    re_path(r'^perms/', include('networkapi.grupo.urls_perms')),
    re_path(r'^aperms/', include('networkapi.grupo.urls_aperms')),
    re_path(r'^direitosgrupoequipamento/',
        include('networkapi.grupo.urls_direitosgrupoequipamento')),

    # filter
    re_path(r'^filter/', include('networkapi.filter.urls')),

    # rack
    re_path(r'^rack/', include('networkapi.rack.urls')),

    # eventlog
    re_path(r'^eventlog/', include('networkapi.eventlog.urls')),

]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
