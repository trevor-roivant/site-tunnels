import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import Tunnel

class TunnelTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    status = ChoiceFieldColumn()
    class Meta(NetBoxTable.Meta):
        model = Tunnel
        fields = ('pk', 'id', 'name', 'sourcedevice','peersite','tenant', 'comments', 'status')
        default_columns = ('name', 'tenant','status')

