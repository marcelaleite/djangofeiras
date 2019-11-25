from django.db import models
from django.contrib import auth
from django.urls import reverse

from gestao_feira.models import Categoria

# Create your models here.

class Certificado(models.Model):
    nome_modelo = models.CharField(max_length=50, null=False, blank=False)
    ptext = models.CharField(max_length=500, null=False, blank=False)
    imagem_fundo = models.ImageField(upload_to="certificados/fundo/", null=True, blank=True)
    imagem_evento = models.ImageField(upload_to="certificados/evento/", null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_modelo

    def get_absolute_url(self):
        return reverse('certificados-detail', kwargs={'pid':self.id})

    def get_model_absolute_url(self):
        return reverse('certificados-model-detail', kwargs={'pid':self.id})
