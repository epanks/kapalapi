from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('balai/', views.balai, name="balai"),
    path('paket/', views.paket, name="paket"),
]