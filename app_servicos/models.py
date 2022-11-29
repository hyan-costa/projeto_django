import decimal
from datetime import datetime
from secrets import token_hex
from django.db import models
from app_clientes.models import Cliente
from app_servicos.choices import ChoicesCategoriaManutencao
from app_funcionario.models import Funcionario

class CONST(object):
    class STATUS(object):
        ABERTA = 1
        EM_ATENDIMENTO = 2
        AGUARDANDO_ORCAMENTO = 3
        FINALIZADO = 4

        choices = (
            (ABERTA, 'ABERTA'),
            (EM_ATENDIMENTO, 'EM ATENDIMENTO'),
            (AGUARDANDO_ORCAMENTO, 'AGUARDANDO ORÇAMENTO'),
            (FINALIZADO, 'FINALIZADO')
        )


class CategoriaManutencao(models.Model):
    titulo = models.CharField(max_length=3, choices=ChoicesCategoriaManutencao.choices)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) ->str:
        return self.titulo

class Servico(models.Model):
    titulo = models.CharField(max_length=60)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    data_inicio = models.DateField(null=True)
    data_entrega = models.DateField(null=True)
    status = models.IntegerField(max_length=1, verbose_name='Status', choices=CONST.STATUS.choices)
    protocolo = models.CharField(max_length=32, null=True, blank=True)
    categoria_manutencao = models.ManyToManyField(CategoriaManutencao)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    def __str__(self) ->str:
        return self.titulo

#-----------------------------------------------------------------------------------------------------------------------
#salva o obj, mas antes analisa se tem o protocolo
#-----------------------------------------------------------------------------------------------------------------------
    def save(self, *args,**kwargs):
        if not self.protocolo:
            self.protocolo = datetime.now().strftime("%d/%m/%Y-%H:%M-") + token_hex(7)
        super(Servico, self).save(*args,**kwargs)
#-----------------------------------------------------------------------------------------------------------------------
#calcula preco total
#-----------------------------------------------------------------------------------------------------------------------
    def preco_total(self):
        total = decimal.Decimal('0.0')
        for valor in self.categoria_manutencao.all():
            total += valor.preco
        return total
