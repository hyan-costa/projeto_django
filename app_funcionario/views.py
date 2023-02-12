import re

from django.contrib.auth.decorators import login_required
from django.db.transaction import on_commit
from django.http import JsonResponse
from django.core import serializers
import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from .models import Funcionario, HistoricoFuncionarios
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.messages import error, success


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

        cpf_valid = re.sub('[.,-]', '', cpf)

        funcionario = Funcionario.objects.filter(cpf=cpf)
        if not funcionario:
            usuario = Funcionario(nome=nome, cpf=cpf_valid, funcao=funcao)
            usuario.save()

        return render(request, 'funcionarios.html', grid_funcionarios())
    else:
        # print(request.user.pk)
        return render(request, 'funcionarios.html', grid_funcionarios())


@csrf_exempt
def apaga_funcionarios(request):
    usuario = request.user
    if request.method == 'POST':
        pk_funcionario = request.POST.get('pk_funcionario')

        funcionario = Funcionario.objects.get(id=pk_funcionario)
        if funcionario:

            historico = HistoricoFuncionarios(
                            usuario=usuario,
                            descricao=u"APAGOU O USUÁRIO {}[{}]".format(funcionario.nome, funcionario.pk),
                            acao='APAGOU'
                        )
            funcionario.delete()
            historico.save()

            result = {'resultado': 'true'}
        else:
            result = {'resultado': 'false'}

    return JsonResponse(result)


# -----------------------------------------------------------------------------------------------------------------------
#valida o cpf do funcionario
# -----------------------------------------------------------------------------------------------------------------------
def valida_funcionarios(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        funcionario = Funcionario.objects.filter(cpf=cpf)
        if funcionario:
            validacao = json.loads(serializers.serialize('json', funcionario))[0]['fields']
            for funcao in Funcionario.funcaoChoices.choices:
                if funcao[0] == validacao['funcao']:
                    validacao['funcao'] = funcao[1]
        elif len(cpf) != 11:
            validacao = {'erro': 'CPF Inválido'}
        else:
            validacao = {'pass': None}
    return JsonResponse(validacao)

# -----------------------------------------------------------------------------------------------------------------------
# Retorna o context para o grid funcionarios com os dados atualizados
# -----------------------------------------------------------------------------------------------------------------------
def grid_funcionarios():
    funcionarios = Funcionario.objects.all()

    context = dict(
        funcionarios=funcionarios,
        choices=Funcionario.funcaoChoices
    )
    return context
