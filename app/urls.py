from django.urls import path, include
from app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('resultado/', views.resultado, name='resultado'),
    path('addcidade/', views.addcidade, name='addcidade'),
    path('contatos/', views.contatos, name='contatos'),
    path('not_found/', views.resultado, name='not_found'),
]
