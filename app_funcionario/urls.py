from django.urls import path, include
from . import views
urlpatterns = [

    #path('get_parametros/', views.get_parametros, name='get_parametros'),
    path('', views.funcionarios, name='funcionarios'),
    path('ajax_validacao/',views.valida_funcionarios,name='ajax_validacao'),
]