# -*- coding: utf-8 -*-
# from django.conf.urls import patterns
# from django.conf.urls import url
from django.urls import re_path

from networkapi.api_ogp import views

urlpatterns = [
    # 'networkapi.api_ogp.views',
    re_path(r'^v3/object-group-perm/((?P<ogp_ids>[;\w]+)/)?$',
        views.ObjectGroupPermView.as_view()),
    re_path(r'^v3/object-group-perm-general/((?P<ogpg_ids>[;\w]+)/)?$',
        views.ObjectGroupPermGeneralView.as_view()),
    re_path(r'^v3/object-type/((?P<ot_ids>[;\w]+)/)?$',
        views.ObjectTypeView.as_view()),
]
