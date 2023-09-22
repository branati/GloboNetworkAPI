# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.rack.resource.RackAplicarConfigResource import RackAplicarConfigResource
from networkapi.rack.resource.RackConfigResource import RackConfigResource
from networkapi.rack.resource.RackDeleteResource import RackDeleteResource
from networkapi.rack.resource.RackEditResource import RackEditResource
from networkapi.rack.resource.RackEnvironmentResource import RackEnvironmentResource
from networkapi.rack.resource.RackFindResource import RackFindResource
from networkapi.rack.resource.RackGetByEquipResource import RackGetByEquipResource
from networkapi.rack.resource.RackListAllResource import RackListAllResource

find_rack_resource = RackFindResource()
edit_rack_resource = RackEditResource()
delete_rack_resource = RackDeleteResource()
gerar_config_rack_resource = RackConfigResource()
aplicar_config_rack_resource = RackAplicarConfigResource()
list_all_racks_resource = RackListAllResource()
list_rack_environment_resource = RackEnvironmentResource()
get_rack_by_equip_resource = RackGetByEquipResource()


urlpatterns = [
    re_path(r'^list[/]?$', list_all_racks_resource.handle_request,
        name='list.rack'),
    re_path(r'^find/(?P<rack_name>[^/]+)/$', find_rack_resource.handle_request,
        name='find.rack'),
    re_path(r'^edit[/]?$', edit_rack_resource.handle_request,
        name='edit.rack'),
    re_path(r'^(?P<id_rack>[^/]+)/$', delete_rack_resource.handle_request,
        name='delete.rack'),
    re_path(r'^gerar-configuracao/(?P<id_rack>[^/]+)/$', gerar_config_rack_resource.handle_request,
        name='config.rack'),
    re_path(r'^alocar-config/(?P<id_rack>[^/]+)/$', aplicar_config_rack_resource.handle_request,
        name='aplicar.rack'),
    re_path(r'^get-by-equip/(?P<equip_id>[^/]+)/$', get_rack_by_equip_resource.handle_request,
        name='rack.get.equip.id'),
    re_path(r'^list-rack-environment/(?P<rack_id>[^/]+)/$', list_rack_environment_resource.handle_request,
        name='interfacetype.get'),
]
