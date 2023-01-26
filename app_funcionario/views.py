import re

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers
import json
from .models import Funcionario
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.messages import error,success
# def get_parametros(request):
#     if request.method == "POST":
#         return render(request,'funcionarios.html')
#     else:
#         return render(request, 'funcionarios.html')
@login_required(login_url="/autenticacao/login")
def funcionarios(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        funcao = request.POST.get('funcao')
        cpf = str(request.POST.get('cpf'))

        cpf_valid = re.sub('[.,-]','',cpf)

        funcionario = Funcionario.objects.filter(cpf=cpf)
        if not funcionario:
            usuario = Funcionario(nome=nome,cpf=cpf_valid, funcao=funcao)
            usuario.save()

        return render(request,'funcionarios.html',grid_funcionarios())
    else:
        return render(request, 'funcionarios.html', grid_funcionarios())

def valida_funcionarios(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        funcionario = Funcionario.objects.filter(cpf=cpf)
        if funcionario:
            validacao = json.loads(serializers.serialize('json', funcionario))[0]['fields']
            for funcao in Funcionario.funcaoChoices.choices:
                if funcao[0] == validacao['funcao']:
                    validacao['funcao'] = funcao[1]
        else:
            validacao = {'pass':None}
    return JsonResponse(validacao)






#-----------------------------------------------------------------------------------------------------------------------
# Retorna o context para o grid funcionarios com os dados atualizados
#-----------------------------------------------------------------------------------------------------------------------
def grid_funcionarios():
    funcionarios = Funcionario.objects.all()

    context = dict(
        funcionarios=funcionarios,
        choices=Funcionario.funcaoChoices
    )
    return context