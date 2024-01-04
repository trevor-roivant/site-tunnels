from extras.plugins import PluginConfig

class NetBoxSiteTunnelsConfig(PluginConfig):
    name = 'netbox_site_tunnels'
    verbose_name = 'NetBox Tunnels'
    description = 'Keep inventory of tunnels'
    version = '0.2'
    base_url = 'site-tunnels'
config = NetBoxSiteTunnelsConfig
