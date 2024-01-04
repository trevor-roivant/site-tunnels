import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import Tunnel

class TunnelTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    sourcedevice = tables.Column(
        linkify=True,
        verbose_name="Source Device"
    )
    sourceip = tables.Column(
        linkify=True,
        verbose_name="Source IP"
    )
    peersite = tables.Column(
        linkify=True,
        verbose_name="Peer Site"
    )
    status = ChoiceFieldColumn()
    class Meta(NetBoxTable.Meta):
        model = Tunnel
        fields = ('pk', 'id', 'name', 'sourcedevice','peersite', 'comments', 'sourceip','status')
        default_columns = ('name', 'status' ,'sourcedevice', 'peersite')

