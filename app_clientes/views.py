import re

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from . import models
from django.core import serializers
import json
def clientes(request):
    if request.method == 'GET':
        td_clientes = models.Cliente.objects.all()
        return render(request,'clientes.html',{'clientes':td_clientes})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')

        carro = request.POST.getlist('carro')
        placa = request.POST.getlist('placa')
        ano = request.POST.getlist('ano')

        cliente = models.Cliente.objects.filter(cpf=cpf)


        tupla = list(zip(carro,placa,ano))

        if cliente.exists():
            return render(request,'clientes.html',{'nome':nome,'sobrenome':sobrenome,'email':email,'carros':tupla})
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'),email):
            return render(request,'clientes.html',{'nome':nome,'sobrenome':sobrenome,'cpf':cpf})

        cliente = models.Cliente(
            nome=nome,
            sobrenome= sobrenome,
            email=email,
            cpf=cpf
        )
        cliente.save()

        for carro, placa, ano in tupla:
            car = models.Carro(carro=carro,placa=placa,ano=ano, cliente_id=cliente.pk)
            car.save()
        return render(request, 'clientes.html')

def att_cliente(request):
    id_cliente = request.POST.get('cliente_pk')
    cliente = models.Cliente.objects.filter(pk=id_cliente)
    cliente_json = json.loads(serializers.serialize('json',cliente))[0]['fields']
    print(cliente_json)
    return JsonResponse(cliente_json)