import re

from app_clientes.cep.cep import add_cep
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from . import models

from django.core import serializers
import json

#-----------------------------------------------------------------------------------------------------------------------
# add clientes
#-----------------------------------------------------------------------------------------------------------------------
def clientes(request):
    if request.method == 'GET':
        td_clientes = models.Cliente.objects.all()
        return render(request,'clientes.html',{'clientes':td_clientes})
    elif request.method == 'POST':
        context = {}
        td_clientes = models.Cliente.objects.all()
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
            messages.error(request, 'Usuário já existente!')
            return render(request,'clientes.html',{'nome':nome,'sobrenome':sobrenome,'email':email,'carros':tupla},)
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'),email):
            messages.error(request, 'email incorreto!')
            return render(request,'clientes.html',{'nome':nome,'sobrenome':sobrenome,'cpf':cpf}, status=500)

        cliente = models.Cliente(
            nome=nome,
            sobrenome= sobrenome,
            email=email,
            cpf=cpf
        )
        cliente.save()
        context['clientes']=td_clientes

        #------------salva o cep do cliente-----------------
        cep = request.POST.get('cep')
        if cep:
            pk = cliente.pk
            add_cep(request,cep,pk)

        #------------salva os carros
        for carro, placa, ano in tupla:
            car = models.Carro(carro=carro,placa=placa,ano=ano, cliente_id=cliente.pk)
            car.save()
        return render(request, 'clientes.html',context)

#-----------------------------------------------------------------------------------------------------------------------
# Retorna o endereco residencial para carregar no front
#-----------------------------------------------------------------------------------------------------------------------
@csrf_exempt
def retorna_cep(request):

    cep = request.POST.get("cep_value")
    cep_valor = add_cep(None,cep,None)

    cep_json = json.dumps(cep_valor)
    cep_json = json.loads(cep_json)

    return JsonResponse(cep_json, safe=False)
#-----------------------------------------------------------------------------------------------------------------------
# retorna os dados do cliente para fazer alteracoes
#-----------------------------------------------------------------------------------------------------------------------
def att_cliente(request):
    id_cliente = request.POST.get('cliente_pk')
    cliente = models.Cliente.objects.filter(pk=id_cliente)
    carros = models.Carro.objects.filter(cliente=cliente[0])

    cliente_json = json.loads(serializers.serialize('json',cliente))[0]['fields']
    carro_json = json.loads(serializers.serialize('json',carros))
    carro_json = [{'fields': x['fields'], 'id_carro':x['pk']}for x in carro_json]

    data = {'cliente':cliente_json, 'carros':carro_json}
    return JsonResponse(data)



#-----------------------------------------------------------------------------------------------------------------------
#aletra dados do carro
#-----------------------------------------------------------------------------------------------------------------------
@csrf_exempt
def update_carro(request,id):
    nome_carro = request.POST.get('carro')
    placa = request.POST.get('placa')
    ano = request.POST.get('ano')
    list_placa = models.Carro.objects.exclude(id=id).filter(placa=placa)

    if list_placa.exists():
        return HttpResponse('placa já existente!')
    carro = models.Carro.objects.get(id=id)
    carro.placa = placa
    carro.ano = ano
    carro.carro = nome_carro
    carro.save()

    context = {'salva_pessoa':'salvo com sucesso!'}
    return redirect(reverse('clientes')+f'?aba=att_cliente&id_cliente={id}',context)


#-----------------------------------------------------------------------------------------------------------------------
# exclui carro
#-----------------------------------------------------------------------------------------------------------------------

def excluir_carro(request, id):
    try:
        carro = models.Carro.objects.get(id=id)
        carro.delete()
        return redirect(reverse('clientes')+f'?aba=att_cliente&id_cliente={id}')
    except:
        return HttpResponse(redirect(reverse('clientes')))