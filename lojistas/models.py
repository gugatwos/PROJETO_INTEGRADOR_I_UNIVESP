from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Produto(models.Model):
    CATEGORIA_CHOICES = [
        ('POTE', 'Sorvete de Pote'),
        ('MASSA', 'Sorvete de Massa'),
        ('PICOLE', 'Picolé'),
    ]
    nome = models.CharField(max_length=50, default = 'sorvete')
    descricao = models.CharField(max_length=300)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=15, choices=CATEGORIA_CHOICES, default='POTE')
    quantidade = models.IntegerField()

    def __str__(self):
        return self.descricao

class Lojista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=300)
    telefone = models.CharField(max_length=20)  # Alterado para CharField
    email = models.CharField(max_length=100)

class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='produtos')
    quantidade = models.IntegerField()

class Vendas(models.Model):
    processo = models.BooleanField()
    lojista = models.ForeignKey(Lojista, on_delete=models.CASCADE)
    valor_produto = models.DecimalField(max_digits=8, decimal_places=2)  # Corrigido nome e aumentado max_digits
