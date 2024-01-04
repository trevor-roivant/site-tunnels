from extras.plugins import PluginMenu , PluginMenuItem, PluginMenuButton
from utilities.choices import ButtonColorChoices
menu_items = (PluginMenuItem(
        link='plugins:netbox_site_tunnels:tunnel_list',
        link_text='Tunnels',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_site_tunnels:tunnel_add',
                title='Tunnels',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,

            ),
        ),
    ),)

