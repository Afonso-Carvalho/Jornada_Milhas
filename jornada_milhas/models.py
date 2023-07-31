from django.db import models
from django.db.models.signals import pre_save
from openai_api.client import get_destino_ai_texto


class Depoimento(models.Model):
    foto = models.ImageField(blank=False)
    nome = models.CharField(max_length=100)
    depoimento = models.TextField(max_length=500)

    def __str__(self):
        return self.nome

class Destino(models.Model):
    foto_principal = models.ImageField(blank=False) 
    foto_secundaria = models.ImageField(blank=True) 
    nome = models.CharField(max_length=100)
    preço = models.IntegerField()
    meta = models.CharField(max_length=160,blank=True)
    texto_descritivo = models.TextField(max_length=200,blank=True)

    def __str__(self):
        return self.nome


def destino_pre_save(sender,instance,**kwargs):
    if not instance.texto_descritivo:
        ia_texto = get_destino_ai_texto(
            instance.nome
        )
        instance.texto_descritivo = ia_texto

pre_save.connect(destino_pre_save,sender=Destino)


