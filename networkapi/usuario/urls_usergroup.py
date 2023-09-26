# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.usuario.resource.UserGroupAssociateResource import UserGroupAssociateResource
from networkapi.usuario.resource.UserGroupDissociateResource import UserGroupDissociateResource

user_group_associate_resource = UserGroupAssociateResource()
user_group_dissociate_resource = UserGroupDissociateResource()

urlpatterns = [
    re_path(r'^user/(?P<id_user>[^/]+)/ugroup/(?P<id_group>[^/]+)/associate/$', user_group_associate_resource.handle_request,
        name='user_group.associate'),
    re_path(r'^user/(?P<id_user>[^/]+)/ugroup/(?P<id_group>[^/]+)/dissociate/$', user_group_dissociate_resource.handle_request,
        name='user_group.dissociate')
]
