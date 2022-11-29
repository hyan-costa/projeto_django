import re

from django.contrib.auth.decorators import login_required
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
            return render(request, 'funcionarios.html')

    elif request.method == "GET":

        return render(request, 'funcionarios.html', grid_funcionarios())




#-----------------------------------------------------------------------------------------------------------------------
# Retorna o context para o grid funcionarios com os dados atualizados
#-----------------------------------------------------------------------------------------------------------------------
def grid_funcionarios():
    funcionarios = Funcionario.objects.all()

    #atribui o a posicao 1 da tupla para o grid
    for funcionario in funcionarios:
        for choices in Funcionario.FuncaoChoices.choices:
            if choices[0] == funcionario.funcao:
                funcionario.funcao = choices[1]

    context = dict(
        funcionarios=funcionarios,
        choices=Funcionario.FuncaoChoices
    )
    return context