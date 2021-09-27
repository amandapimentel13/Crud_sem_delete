from django.db import models

# Models.
from django.db import models

# Create models here.
class Empresa(models.Model):
    Nome = models.CharField(max_length=150)
    Contato = models.CharField(max_length=100)
    Telefone = models.IntegerField()

    def __str__(self):
        return self.Nome + " - " + self.Contato + " - " +str(self.Telefone) + " - "


class Produto(models.Model):
    NomeProd = models.CharField(max_length=150)
    Marca = models.CharField(max_length=100)
    Preco = models.IntegerField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)