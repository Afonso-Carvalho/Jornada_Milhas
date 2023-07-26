from django.db import models

class Depoimento(models.Model):
    foto = models.ImageField(blank=False)
    nome = models.CharField(max_length=100)
    depoimento = models.TextField(max_length=500)

    def __str__(self):
        return self.nome

class Destino(models.Model):
    foto = models.ImageField(blank=False)
    nome = models.CharField(max_length=100)
    preço = models.IntegerField()

    def __str__(self):
        return self.nome


