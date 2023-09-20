# -*- coding: utf-8 -*-
from __future__ import absolute_import

# from django.conf.urls import patterns
# from django.conf.urls import url

from django.urls import re_path

from networkapi.healthcheckexpect.resource.HealthcheckAddExpectStringResource import HealthcheckAddExpectStringResource
from networkapi.healthcheckexpect.resource.HealthcheckAddResource import HealthcheckAddResource
from networkapi.healthcheckexpect.resource.HealthcheckExpectDistinctResource import HealthcheckExpectDistinctResource
from networkapi.healthcheckexpect.resource.HealthcheckExpectGetResource import HealthcheckExpectGetResource
from networkapi.healthcheckexpect.resource.HealthcheckExpectResource import HealthcheckExpectResource

healthcheckexpect_resource = HealthcheckExpectResource()
healthcheckexpect_add_resource = HealthcheckAddResource()
healthcheckexpect_string_resource = HealthcheckAddExpectStringResource()
healthcheckexpect_distinct_resource = HealthcheckExpectDistinctResource()
healthcheckexpect_get_resource = HealthcheckExpectGetResource()

urlpatterns = [
    re_path(r'^ambiente/(?P<id_amb>[^/]+)/$', healthcheckexpect_resource.handle_request,
            name='healthcheckexpect.search.by.environment'),
    re_path(r'^add/$', healthcheckexpect_add_resource.handle_request,
            name='healthcheckexpect.add'),
    re_path(r'^add/expect_string/$', healthcheckexpect_string_resource.handle_request,
            name='healthcheckexpect.string.add'),
    re_path(r'^distinct/busca/$', healthcheckexpect_distinct_resource.handle_request,
            name='healthcheckexpect.distinct'),
    re_path(r'^get/(?P<id_healthcheck>[^/]+)/$', healthcheckexpect_get_resource.handle_request,
            name='healthcheckexpect.get.by.pk')
]
