from django.contrib.contenttypes.models import ContentType



from dcim.api.nested_serializers import WritableNestedSerializer
from dcim.api.serializers import DeviceWithConfigContextSerializer
from tenancy.api.nested_serializers import NestedTenantSerializer
from dcim.models.devices import Device, Interface
from drf_yasg.utils import swagger_serializer_method
from ipam.api.nested_serializers import *
from ipam.models.ip import IPAddress
from netaddr import IPNetwork
from rest_framework import serializers
from rest_framework.utils import json
from netbox.api import ChoiceField, ContentTypeField, SerializedPKRelatedField
from ipam.choices import *
from ipam.constants import IPADDRESS_ASSIGNMENT_MODELS


class NestedIPAddressSerializer(WritableNestedSerializer):
    class Meta:

        model = IPAddress

        vrf = NestedVRFSerializer(required=False, allow_null=True)
        tenant = NestedTenantSerializer(required=False, allow_null=True)
        status = ChoiceField(choices=IPAddressStatusChoices, required=False)
        role = ChoiceField(choices=IPAddressRoleChoices, allow_blank=True, required=False)
        assigned_object_type = ContentTypeField(
            queryset=ContentType.objects.filter(IPADDRESS_ASSIGNMENT_MODELS),
            required=False,
            allow_null=True
        )
        # assigned_object = serializers.SerializerMethodField(read_only=True)
        nat_inside = NestedIPAddressSerializer(required=False, allow_null=True)
        nat_outside = NestedIPAddressSerializer(read_only=True)
        fields = [
            'id',  'display', 'family', 'address', 'vrf', 'tenant', 'status', 'role', 'assigned_object_type',
            'assigned_object_id', 'nat_inside', 'nat_outside', 'dns_name', 'description',
            'created', 'last_updated',
            ]

        fields.extend([
            "address","vrf"

        ])

class NestedInterfaceSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='dcim-api:interface-detail')

    ip_addresses_set = NestedIPAddressSerializer(many=True, read_only=True,source='ip_addresses')

    primary_ip = serializers.SerializerMethodField()
    primary_vrf = serializers.SerializerMethodField()
    router = serializers.SerializerMethodField()

    class Meta:
        model = Interface

        fields = [
            'id', 'url', 'display', 'device', 'name', 'label', 'type', 'enabled', 'parent', 'lag', 'mtu', 'mac_address',
            'mgmt_only', 'description', 'mode', 'untagged_vlan', 'tagged_vlans', 'mark_connected', 'cable',
            'created', 'last_updated', 'count_ipaddresses',
            '_occupied',
        ]

        fields.extend(["ip_addresses_set","primary_ip","primary_vrf","router"])

        # fields = [
        #     "id", "name","mgmt_only","mac_address","untagged_vlan_id","mtu","lag_id","mode","ip_addresses_set","primary_ip","primary_vrf","router"
        # ]

    @swagger_serializer_method(serializer_or_field=serializers.DictField)
    def get_primary_ip(self, obj):
        ips = IPAddress.objects.filter(assigned_object_id=obj.id)
        for ip in  ips:
            return ip.address

    @swagger_serializer_method(serializer_or_field=serializers.DictField)
    def get_primary_vrf(self, obj):
        ips = IPAddress.objects.filter(assigned_object_id=obj.id)
        for ip in  ips:
            if ip.vrf is not None:
                return ip.vrf.name

    @swagger_serializer_method(serializer_or_field=serializers.DictField)
    def get_router(self, obj):
        ips = IPAddress.objects.filter(assigned_object_id=obj.id)
        for ip in  ips:
            network  = IPNetwork(ip.address)
            return network[0]+1

class DeviceSerializer(DeviceWithConfigContextSerializer):

    config_context = serializers.SerializerMethodField()
    ntp_servers = serializers.SerializerMethodField()

    interface_set = NestedInterfaceSerializer(many=True, read_only=True,source='interfaces')
    class Meta:
        model = Device
        fields = [
            'id', 'url', 'display', 'name', 'display_name', 'device_type', 'device_role', 'tenant', 'platform',
            'serial', 'asset_tag', 'site', 'location', 'rack', 'position', 'face', 'parent_device', 'status',
            'primary_ip', 'primary_ip4', 'primary_ip6', 'cluster', 'virtual_chassis', 'vc_position', 'vc_priority',
            'comments', 'local_context_data',  'custom_fields', 'created', 'last_updated'
        ]

        fields.extend(['config_context','ntp_servers','interface_set'])

        # fields = [
        #     'id',  'name', 'display_name', 'device_type', 'device_role', 'tenant', 'platform',
        #     'serial', 'local_context_data', 'tags', 'config_context','ntp_servers','interface_set', 'created', 'last_updated',
        # ]


    @swagger_serializer_method(serializer_or_field=serializers.DictField)
    def get_config_context(self, obj):
        return obj.get_config_context()

    @swagger_serializer_method(serializer_or_field=serializers.DictField)
    def get_ntp_servers(self, obj):
        ntp_ips = []
        ntps  = self.get_config_context(obj).get('cc').get('net').get('service').get('ntp')
        if ntps is not None:
            for ntp in ntps:
                ntp_ips.append(ntp.get('ip'))

        return ntp_ips

