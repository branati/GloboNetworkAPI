# -*- coding: utf-8 -*-
# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.api_rest import views

urlpatterns = [
    # 'networkapi.api_rest.views',
    re_path(r'^v3/help/(?P<way>[_\w]+)/$', views.HelperApi.as_view()),  # GET
]
