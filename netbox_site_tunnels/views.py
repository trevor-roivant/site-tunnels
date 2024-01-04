from netbox.views import generic
from . import forms, models, tables
from utilities.views import ViewTab, register_model_view
from dcim.models import SiteGroup

class TunnelView(generic.ObjectView):
    queryset = models.Tunnel.objects.all()


class TunnelListView(generic.ObjectListView):
    queryset = models.Tunnel.objects.all()
    table = tables.TunnelTable

class TunnelEditView(generic.ObjectEditView):
    queryset = models.Tunnel.objects.all()
    form = forms.TunnelForm

class TunnelDeleteView(generic.ObjectDeleteView):
    queryset = models.Tunnel.objects.all()


