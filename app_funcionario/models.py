from django.db import models

class Funcionario(models.Model):
    class funcaoChoices(models.TextChoices):
        GERENTE =               1, 'Gerente'
        AUXILIAR_TEC =          2, 'Auxiliar Técnico'
        MECANICO =              3, 'Mecânico'
        ENGENHEIRO_MECANICO =   4, 'Engenheiro Mecânico'
        JOVEM_APRENDIZ =        5, 'Jovem Aprendiz'
        ATENDENTE =             6, 'Atendente'
        LAVADOR =               7, 'Lavador'

    nome = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11, unique=True,null=False,blank=False)
    funcao = models.CharField(max_length=60, choices= funcaoChoices.choices)
    tag_id = models.CharField(max_length=11,unique=True, null=True)

    def __str__(self) ->str:
        return self.nome
