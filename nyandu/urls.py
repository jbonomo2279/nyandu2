from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('prueba', views.index, name='index'),
    path('', views.principal, name='principal'),
    ##path('ingreso', auth_views.LoginView.as_view(template_name='nyandu/ingreso.html'), name='login'),

]