# -*- coding: utf-8 -*-
# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.api_task import views

urlpatterns = [
    re_path(r'^v3/task/(?P<task_id>[\w\d\-\.]+)/$', views.TaskView.as_view()),
]
