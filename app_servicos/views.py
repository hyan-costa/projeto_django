from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import FormServico

@login_required(login_url="/autenticacao/login")
def novo_servico(request):
    form = FormServico
    return render(request, 'novo_servico.html', {'form': form})