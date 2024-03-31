from django.db import models
from django.contrib.auth.models import User

class Lojista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_da_loja = models.CharField(max_length=255)

class Estoque(models.Model):
    lojista = models.ForeignKey(Lojista, on_delete=models.CASCADE)
    produto = models.CharField(max_length=255)
    quantidade = models.IntegerField()
