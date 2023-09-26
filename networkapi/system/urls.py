# -*- coding: utf-8 -*-
# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.system.views import VariablebyPkView
from networkapi.system.views import VariableView

urlpatterns = [
    # 'networkapi.system.views',
    re_path(r'^system/variables/$', VariableView.as_view()),
    re_path(
        r'^system/variables/(?P<variable_id>[^/]+)/$', VariablebyPkView.as_view()),
]
