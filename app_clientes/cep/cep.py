import requests
from app_clientes.models import Endereco, Cliente
#-----------------------------------------------------------------------------------------------------------------------
# essa funcao retorna um dict com endereco do cep somente se pk==None. Caso seja passada a pk, os dados será salvo no banco
#                                       pk == fk_cliente_id
#-----------------------------------------------------------------------------------------------------------------------
def add_cep(request,cep,pk):
    url_cep = 'https://viacep.com.br/ws/'+ cep +'/json/'
    cep_json = requests.get(url_cep).json()
    if pk:
        uf = request.POST.get('uf')
        localidade = request.POST.get('localidade')
        logradouro = request.POST.get('logradouro')
        cliente = Cliente.objects.get(pk=pk)

        dados = Endereco(pessoa=cliente, localidade=localidade, logradouro=logradouro, uf=uf)
        dados.save()
    else:
        endereco = dict(localidade=cep_json['localidade'], logradouro=cep_json['logradouro'],uf=cep_json['uf'])
        return endereco