from django.urls import path, include
from . import views
urlpatterns = [

    #path('get_parametros/', views.get_parametros, name='get_parametros'),
    path('', views.funcionarios, name='funcionarios'),
    path('ajax_validacao/',views.valida_funcionarios,name='ajax_validacao'),
    path('apaga_funcionario/',views.apaga_funcionarios,name='apaga_funcionario'),
    #path('editar_funcionario/',views.editar_funcionarios,name='editar_funcionario'),
]