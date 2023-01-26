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
            user = User.objects.filter(email=email)
            if not user:
                if len(request.POST) == 5 and senha == conf_senha:
                    User.objects.create_user(nome,email,senha)
                    context=dict(alerta='Usuário criado com sucesso!!', class_alerta='alert-success')
                    return render(request,'login.html',context)
                else:
                    context = dict(class_alerta='alert-warning')
                    messages.error(request, 'As senhas não condisem!!')
                    return render(request, 'create_user.html', context)
            else:
                    context = dict(class_alerta='alert-warning')
                    messages.error(request, 'Usuário já existe!!')
                    return render(request, 'create_user.html', context)

        except:
            messages.error(request,'Erro, contate o suporte técnico!')
            return render(request, 'create_user.html')

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
                context = dict(class_alerta='alert-warning')
                return render(request,'login.html', context)
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
    if user.check_password(password):
        return user
    return None