from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import Tunnel


class NestedTunnelSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_site_tunnels-api:tunnel-detail'
    )

    class Meta:
        model = Tunnel
        fields = ('id', 'url', 'display', 'name')


class TunnelSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_site_tunnels-api:tunnel-detail'
    )
    class Meta:
        model = Tunnel
        fields = (
            'id', 'url', 'name', 'display', 'tenant', 'comments', 'contact','contactgroup', 'sourcedevice','sourceip','peerip','peersite', 'status', 'tags', 'created',
            'last_updated',
        )
        sitegroup = NestedTunnelSerializer()


        