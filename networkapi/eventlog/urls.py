# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.eventlog.resource.EventLogChoiceResource import EventLogChoiceResource
from networkapi.eventlog.resource.EventLogFindResource import EventLogFindResource

eventlog_find_resource = EventLogFindResource()
eventlog_choice_resource = EventLogChoiceResource()

urlpatterns = [
    re_path(r'^find/$', eventlog_find_resource.handle_request,
        name='eventlog.find'),
    re_path(r'^choices/$', eventlog_choice_resource.handle_request,
        name='eventlog.choices'),
    re_path(r'^version/$', eventlog_find_resource.handle_request,
        name='eventlog.version')
]
