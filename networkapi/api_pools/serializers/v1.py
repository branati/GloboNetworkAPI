# -*- coding: utf-8 -*-
from rest_framework import serializers

from networkapi.ambiente.models import Ambiente
from networkapi.api_network.serializers.v1 import Ipv4Serializer
from networkapi.api_network.serializers.v1 import Ipv6Serializer
from networkapi.api_pools.models import OpcaoPoolAmbiente
from networkapi.api_pools.models import OptionPool
from networkapi.api_pools.models import OptionPoolEnvironment
from networkapi.equipamento.models import Equipamento
from networkapi.healthcheckexpect.models import Healthcheck
from networkapi.infrastructure.script_utils import exec_script
from networkapi.requisicaovips.models import ServerPool
from networkapi.requisicaovips.models import ServerPoolMember
from networkapi.requisicaovips.models import VipPortToPool
from networkapi.settings import POOL_REAL_CHECK


class HealthcheckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Healthcheck
        fields = (
            'id',
            'identifier',
            'healthcheck_type',
            'healthcheck_request',
            'healthcheck_expect',
            'destination'
        )


class ServerPoolDatatableSerializer(serializers.ModelSerializer):

    healthcheck = HealthcheckSerializer()

    environment = serializers.RelatedField(source='environment.name', read_only=True)
    maxcom = serializers.CharField(source='default_limit')
    vip_port = serializers.SerializerMethodField('get_vip_port')

    class Meta:
        model = ServerPool
        fields = (
            'id',
            'identifier',
            'default_port',
            'healthcheck',
            'environment',
            'pool_created',
            'lb_method',
            'maxcom',
            'vip_port'
        )

    def get_vip_port(self, obj):

        return obj.vip_ports[0].port_vip if obj.vip_ports else 0

    # def get_vip_ports(self, obj):
    #
    #     return [p.port_vip for p in obj.vip_ports]


class EquipamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipamento
        fields = (
            'id',
            'tipo_equipamento',
            'modelo',
            'nome',
            'grupos'
        )


class ServerPoolMemberSerializer(serializers.ModelSerializer):

    # pool_enabled = serializers.SerializerMethodField('check_pool_member_enabled')
    equipment_name = serializers.SerializerMethodField('get_name_equipment')
    equipment_id = serializers.SerializerMethodField('get_id_equipment')
    last_status_update_formated = serializers.Field(
        source='last_status_update_formated')

    ip = Ipv4Serializer()
    ipv6 = Ipv6Serializer()

    class Meta:
        depth = 1
        model = ServerPoolMember
        fields = (
            'id',
            'server_pool',
            'identifier',
            'ipv6', 'ip',
            'priority',
            'weight',
            'limit',
            'port_real',
            'healthcheck',
            'member_status',
            'last_status_update',
            'last_status_update_formated',
            'equipment_name',
            'equipment_id',
        )

    def check_pool_member_enabled(self, obj):

        command = POOL_REAL_CHECK % (
            obj.server_pool.id, obj.ip.id, obj.port_real)

        code, _, _ = exec_script(command)

        if code == 0:
            return True

        return False

    def get_name_equipment(self, obj):

        return obj.equipment.nome

    def get_id_equipment(self, obj):

        return obj.equipment.id


class ServerPoolSerializer(serializers.ModelSerializer):

    class Meta:
        depth = 1
        model = ServerPool
        fields = (
            'id',
            'identifier',
            'default_port',
            'default_limit',
            'healthcheck',
            'servicedownaction',
            'environment',
            'pool_created',
            'lb_method'
        )


class PoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServerPool
        fields = (
            'id',
            'identifier',
            'default_port',
            'healthcheck',
            'environment',
            'pool_created'
        )


class OpcaoPoolAmbienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = OpcaoPoolAmbiente
        depth = 1
        fields = (
            'id',
            'opcao_pool',
            'ambiente'
        )


class OptionPoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = OptionPool
        depth = 1
        fields = (
            'id',
            'type',
            'name'
        )


class OptionPoolEnvironmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = OptionPoolEnvironment
        depth = 1
        fields = (
            'id',
            'option',
            'environment'
        )


class VipPortToPoolSerializer(serializers.ModelSerializer):

    environment_vip_ipv4 = serializers.RelatedField(
        source='requisicao_vip.ip.networkipv4.ambient_vip.name',
        read_only=True
    )

    environment_vip_ipv6 = serializers.RelatedField(
        source='requisicao_vip.ipv6.networkipv6.ambient_vip.name',
        read_only=True
    )

    class Meta:
        model = VipPortToPool
        depth = 2
        fields = (
            'id',
            'requisicao_vip',
            'server_pool',
            'port_vip',
            'environment_vip_ipv4',
            'environment_vip_ipv6'
        )


class AmbienteSerializer(serializers.ModelSerializer):

    name = serializers.Field(source='name')

    class Meta:
        model = Ambiente


class ServerPoolMemberStatusSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField('check_pool_member_status')

    class Meta:
        depth = 1
        model = ServerPoolMember
        fields = (
            'id',
            'status',
        )

    def check_pool_member_status(self, obj):

        command = POOL_REAL_CHECK % (
            obj.server_pool.id, obj.ip.id, obj.port_real)

        code, _, _ = exec_script(command)

        return code
