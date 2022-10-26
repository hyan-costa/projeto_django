import requests
from app_clientes.models import Endereco, Cliente
def add_cep(cep,pk):
    url_cep = 'https://viacep.com.br/ws/'+ cep +'/json/'
    cep_json = requests.get(url_cep).json()
    cliente = Cliente.objects.get(pk=pk)
    dados = Endereco(pessoa=cliente, localidade=cep_json['localidade'], logradouro=cep_json['logradouro'], uf=cep_json['uf'])
    dados.save()