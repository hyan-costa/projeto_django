from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.clientes, name='clientes'),
    path('atualiza_cliente/', views.att_cliente, name='atualiza_cliente'),
    path('update_carro/<int:id>', views.update_carro, name='update_carro'),
    path('excluir_carro/<int:id>', views.excluir_carro, name='excluir_carro'),
    path('retorna_cep', views.retorna_cep, name='retorna_cep'),
]