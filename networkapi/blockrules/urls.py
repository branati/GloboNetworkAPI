# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.blockrules.resource.RuleGetResource import RuleGetResource
from networkapi.blockrules.resource.RuleResource import RuleResource

rule_resource = RuleResource()
rule_get_resource = RuleGetResource()

urlpatterns = [
    re_path(r'^get_by_id/(?P<id_rule>[^/]+)/$', rule_resource.handle_request,
        name='rule.get.by.id'),
    re_path(r'^all/(?P<id_env>[^/]+)/$', rule_get_resource.handle_request,
        name='rule.all'),
    re_path(r'^save/$', rule_resource.handle_request,
        name='rule.save'),
    re_path(r'^update/$', rule_resource.handle_request,
        name='rule.update'),
    re_path(r'^delete/(?P<id_rule>[^/]+)/$', rule_resource.handle_request,
        name='rule.delete')
]
