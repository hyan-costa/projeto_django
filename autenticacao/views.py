from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages


def create_user(request):
    if request.method == 'GET':
        return render(request, 'create_user.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        conf_senha = request.POST.get('confirma_senha')

        try:
            if User.objects.filter(username=nome) is not None:
                if len(request.POST) == 5 and senha == conf_senha:
                    User.objects.create_user(nome,email,senha)
                    context=dict(alerta='Usuário criado com sucesso!!')
                    return render(request,'login.html',context)
                else:
                    messages.error(request, 'As senhas não condisem ou você esqueceu algum campo')
                    return redirect('autenticacao_create_user')
            else:
                    messages.error(request, 'Usuário já existe!!')
                    return redirect('autenticacao_create_user')

        except:
            messages.error(request,'Erro, contate o suporte técnico!')
            return redirect('autenticacao_create_user')

def login_view(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        try:
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            usuario = authenticate_user(email=email,password=senha)
            if usuario is not None:
                login(request,usuario)
                return redirect('clientes')
            else:
                messages.error(request,'usuário ou senha inválidos!!')
                return render(request,'login.html')
        except:
            return render(request,'login.html')



@login_required
def logout_view(request):
    logout(request)
    return redirect('login_view')


#-----------------------------------------------------------------------------------------------------------------------
# Função para retornar o usuário, caso haja.
#-----------------------------------------------------------------------------------------------------------------------
def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user
    return None