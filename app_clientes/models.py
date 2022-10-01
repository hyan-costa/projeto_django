from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    def __str__(self) -> str:
        return self.nome


class Carro(models.Model):
    carro = models.CharField(max_length=150)
    placa = models.CharField(max_length=12)
    ano = models.DateTimeField(blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    lavagens = models.IntegerField(default=0)
    consertos = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.carro