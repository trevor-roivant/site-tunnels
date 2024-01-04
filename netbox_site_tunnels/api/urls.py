from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_site_tunnel'

router = NetBoxRouter()
router.register('tunnel', views.TunnelViewSet)
urlpatterns = router.urls