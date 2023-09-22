# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import include
# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.ip.resource.IPv6AddResource import IPv6AddResource
from networkapi.ip.resource.Ipv6AssocEquipResource import Ipv6AssocEquipResource
from networkapi.ip.resource.Ipv6AssociateResource import Ipv6AssociateResource
from networkapi.ip.resource.IPv6DeleteResource import IPv6DeleteResource
from networkapi.ip.resource.IPv6EditResource import IPv6EditResource
from networkapi.ip.resource.IPv6GetResource import IPv6GetResource
from networkapi.ip.resource.Ipv6RemoveResource import Ipv6RemoveResource
from networkapi.ip.resource.IPv6SaveResource import IPv6SaveResource
from networkapi.ip.resource.SearchIPv6EnvironmentResource import SearchIPv6EnvironmentResource

ipv6_edit_resource = IPv6EditResource()
ipv6_get_by_id_resource = IPv6GetResource()
ipv6_delete_resource = IPv6DeleteResource()
ipv6_save_resource = IPv6SaveResource()
ipv6_add_resource = IPv6AddResource()
ipv6_associate = Ipv6AssociateResource()
ipv6_remove = Ipv6RemoveResource()
search_ipv6_environment = SearchIPv6EnvironmentResource()
ipv6_assoc_equip_resource = Ipv6AssocEquipResource()

urlpatterns = [
    re_path(r'^edit',
        ipv6_edit_resource.handle_request, name='ip6.edit'),
    re_path(r'^get/(?P<id_ipv6>[^/]+)/',
        ipv6_get_by_id_resource.handle_request, name='ip6.get.by.id'),
    re_path(r'^delete/(?P<id_ipv6>[^/]+)',
        ipv6_delete_resource.handle_request, name='ip6.delete'),
    re_path(r'^save/$',
        ipv6_save_resource.handle_request, name='ipv6.save'),
    re_path(r'^$', ipv6_add_resource.handle_request,
        name='ipv6.insert'),
    re_path(r'^(?P<id_ipv6>[^/]+)/equipment/(?P<id_equip>[^/]+)/$',
        ipv6_associate.handle_request, name='ipv6equipment.associate'),
    re_path(r'^(?P<id_ipv6>[^/]+)/equipment/(?P<id_equip>[^/]+)/remove/$',
        ipv6_remove.handle_request, name='ipv6equipment.remove'),
    re_path(r'^environment/$', search_ipv6_environment.handle_request,
        name='ipv6.get.by.ip.environment'),
    re_path(r'^assoc/$', ipv6_assoc_equip_resource.handle_request,
        name='ipv6.assoc.equip'),

]
