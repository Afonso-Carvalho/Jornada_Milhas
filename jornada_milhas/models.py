from django.db import models

class Depoimento(models.Model):
    foto = models.ImageField(upload_to="setup/assets/galeria",blank=False)
    nome = models.CharField(max_length=100)
    depoimento = models.TextField(max_length=500)

    def __str__(self):
        return self.nome
