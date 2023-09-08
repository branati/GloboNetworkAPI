# -*- coding: utf-8 -*-
#from django.conf.urls import patterns
#from django.conf.urls import url
from django.urls import re_path

from networkapi.api_aws import views

urlpatterns = [
    # 'networkapi.api_aws.views',
    re_path(r'^v3/aws/vpc((?P<vrf_ids>[;\w]+)/)?$',
        views.AwsVpcView.as_view()),

]
