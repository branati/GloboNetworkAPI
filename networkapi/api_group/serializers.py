# -*- coding: utf-8 -*-
from django.apps import apps
from rest_framework import serializers

from networkapi.util.serializers import DynamicFieldsModelSerializer


class UserGroupV3Serializer(DynamicFieldsModelSerializer):

    name = serializers.Field(source='nome')

    class Meta:
        UGrupo = apps.get_model('grupo', 'UGrupo')
        model = UGrupo
        fields = (
            'id',
            'name'
        )


class EquipmentGroupV3Serializer(DynamicFieldsModelSerializer):

    name = serializers.Field(source='nome')

    class Meta:
        UGrupo = apps.get_model('grupo', 'EGrupo')
        model = UGrupo
        fields = (
            'id',
            'name'
        )
