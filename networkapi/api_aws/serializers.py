# -*- coding: utf-8 -*-
# from django.apps import apps
from django.apps import apps
from networkapi.util.serializers import DynamicFieldsModelSerializer


class AwsVPCSerializer(DynamicFieldsModelSerializer):

    class Meta:
        VPC = apps.get_model('api_aws', 'VPC')
        depth = 1
        model = VPC

        fields = (
            'id',
            'vpc'
        )

        default_fields = fields

        basic_fields = fields

        details_fields = fields
