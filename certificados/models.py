from django.db import models
from django.contrib import auth
from django.urls import reverse

# Create your models here.

class Certificado(models.Model):
    ptext = models.CharField(max_length=500, null=False, blank=False)
    imagem_fundo = models.ImageField(upload_to="certificados/fundo/", null=True, blank=True)
    imagem_evento = models.ImageField(upload_to="certificados/evento/", null=True, blank=True)

    def get_absolute_url(self):
        return reverse('certificados-detail', kwargs={'pid':self.id})

    def get_admin_absolute_url(self):
        return reverse('certificados-admin-detail', kwargs={'pid':self.id})
