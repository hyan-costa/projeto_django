import re

from django.contrib.auth.decorators import login_required
from .models import Funcionario
from django.shortcuts import render, redirect
from django.contrib.messages import error,success
# def get_parametros(request):
#     if request.method == "POST":
#         return render(request,'funcionarios.html')
#     else:
#         return render(request, 'funcionarios.html')
@login_required(login_url="/autenticacao/login")
def funcionarios(request):
    if request.method == "POST":
        num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        nome = request.POST.get('nome')
        cpf = str(request.POST.get('cpf'))
        cpf_valid = re.sub('[.,-]','',cpf)
        # for caractere in cpf_valid:
        #     if not caractere in num:
        #         error(request,'CPF inválido!')
        #         return render(request,'funcionarios.html')
        funcionario = Funcionario.objects.filter(cpf=cpf)

        if not funcionario:
            usuario = Funcionario(nome=nome,cpf=cpf_valid)
            usuario.save()
            return render(request,'funcionarios.html')
        else:
            return render(request, 'funcionarios.html')
    elif request.method == "GET":
        funcionarios = Funcionario.objects.all()
        context = dict(
            funcionarios= funcionarios
        )
        return render(request, 'funcionarios.html', context)