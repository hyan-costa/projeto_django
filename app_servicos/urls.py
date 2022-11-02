from django.urls import path, include
from . import views
urlpatterns = [

    path('novo_servico', views.novo_servico, name='novo_servico'),


]