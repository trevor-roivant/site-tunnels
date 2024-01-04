from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from .choices import AccountStatusChoices
from django.urls import reverse

class Tunnel(NetBoxModel):
    name = models.CharField(
        max_length=32
    )

    display = models.CharField(
        max_length=32,
        blank=True,
        null=True
        )

    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=50,
        choices=AccountStatusChoices,
        default=AccountStatusChoices.STATUS_ACTIVE
    )
    contact = models.ForeignKey(
        help_text='Account Owner',
        to='tenancy.Contact',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True,
    )
    contactgroup = models.ForeignKey(
        help_text='Account Owner',
        to='tenancy.contactgroup',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True,
    )
    sourcedevice = models.ForeignKey(
        help_text='Source Device',
        to='dcim.device',
        on_delete=models.PROTECT,
        related_name="+",
        blank=True,
        null=True
    )
    peersite = models.ForeignKey(
        help_text='Peer Site',
        to='dcim.site',
        on_delete=models.PROTECT,
        related_name="+",
        blank=True,
        null=True
    )

    peerip = models.ForeignKey(
        help_text='Peer IP',
        to='ipam.ipaddress',
        on_delete=models.PROTECT,
        related_name="+",
        blank=True,
        null=True
    )

    sourceip = models.ForeignKey(
        help_text='Source IP',
        to='ipam.ipaddress',
        on_delete=models.PROTECT,
        related_name="+",
        blank=True,
        null=True
    )


    description = models.CharField(
        max_length=200,
        blank=True
    )
    comments = models.TextField(
        blank=True
    )
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('plugins:netbox_site_tunnels:tunnel', args=[self.pk])
    def get_status_color(self):
        return AccountStatusChoices.colors.get(self.status)
