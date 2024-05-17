from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('prueba', views.index, name='index'),
    path('', views.principal, name='principal'),
    ##path('ingreso', auth_views.LoginView.as_view(template_name='nyandu/ingreso.html'), name='login'),
    path('vuelos/', views.VueloListView.as_view(), name='vuelos'),
    path('vuelos/<int:pk>', views.VueloDetailView.as_view(), name='vuelo-detail'),
    path('aviones/', views.AvionListView.as_view(), name='aviones'),
    path('aviones/<int:pk>', views.AvionDetailView.as_view(), name='avion-detail'),

]