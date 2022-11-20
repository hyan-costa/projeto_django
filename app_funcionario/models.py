from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11, unique=True,null=False,blank=False)
    tag_id = models.CharField(max_length=11,unique=True, null=True)

    def __str__(self) ->str:
        return self.nome
