from django.urls import path

from . import views

# app_name = "netbox-zero"

urlpatterns = [
    path('site_topology/', views.SiteTopologyView.as_view(), name='site_topology'),
    path('root', views.RootView.as_view(), name='root'),
]
