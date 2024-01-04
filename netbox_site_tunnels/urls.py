from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView

urlpatterns = (
    path('tunnels/', views.TunnelListView.as_view(), name='tunnel_list'),
    path('tunnels/add/', views.TunnelEditView.as_view(), name='tunnel_add'),
    path('tunnels/<int:pk>/', views.TunnelView.as_view(), name='tunnel'),
    path('tunnels/<int:pk>/edit/', views.TunnelEditView.as_view(), name='tunnel_edit'),
    path('tunnels/<int:pk>/delete/', views.TunnelDeleteView.as_view(), name='tunnel_delete'),
    path('tunnels/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='tunnel_changelog', kwargs={
        'model': models.Tunnel
    })
    
    
)