from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.clientes, name='clientes'),
    path('atualiza_cliente/', views.att_cliente, name='atualiza_cliente'),
]