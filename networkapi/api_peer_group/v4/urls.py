# -*- coding: utf-8 -*-
# from django.conf.urls import patterns
# from django.conf.urls import url
from django.urls import re_path

from networkapi.api_peer_group.v4 import views

urlpatterns = [
    re_path(r'^peer-group/((?P<obj_ids>[;\w]+)/)?$',
        views.PeerGroupDBView.as_view()),
]
