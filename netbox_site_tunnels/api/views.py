from netbox.api.viewsets import NetBoxModelViewSet
from .. import models
from .serializers import TunnelSerializer


class TunnelViewSet(NetBoxModelViewSet):
    queryset = models.Tunnel.objects.prefetch_related('tags')
    serializer_class = TunnelSerializer

