from netbox.forms import NetBoxModelForm
from .models import Tunnel
from django import forms
from tenancy.models import ContactGroup, Contact, Tenant
from dcim.models import Site, Device
from ipam.models import IPAddress
from utilities.forms.fields import (
    DynamicModelChoiceField, CSVModelChoiceField,
    DynamicModelMultipleChoiceField,
    TagFilterField, CSVChoiceField, CommentField,
)

class TunnelForm(NetBoxModelForm):

    contactgroup = DynamicModelChoiceField(
        queryset=ContactGroup.objects.all(),
        label='Contact Group',
        required=False
    )
    contact = DynamicModelChoiceField(
        queryset=Contact.objects.all(),
        label='Contact',
        required=False
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        label='Tenant',
        required=False
    )
    peersite = DynamicModelChoiceField(
        queryset=Site.objects.all(),
        label='Peer Site',
        required=True
    )
    sourcedevice = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        label='Source Device',
        required=True
    )
    sourceip = DynamicModelChoiceField(
        queryset=IPAddress.objects.all(),
        label='Source IP',
        required=True
    )
    peerip = DynamicModelChoiceField(
        queryset=IPAddress.objects.all(),
        label='Peer IP',
        required=True
    )
    comments = CommentField()
    class Meta:
        model = Tunnel
        fields = ('name', 'status' , 'description', 'tenant', 'contact','contactgroup','peersite','peerip','sourcedevice','sourceip')
