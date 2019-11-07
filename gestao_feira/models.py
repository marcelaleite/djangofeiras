from django.db import models
from django.contrib import auth
from django.urls import reverse
from django.conf import settings

class Feira(models.Model):
    nome_feira = models.CharField(max_length=120)
    area = models.CharField(max_length=120)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    cep = models.CharField(max_length=120)
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=120)
    bairro = models.CharField(max_length=120)
    endereco = models.CharField(max_length=120)
    complemento = models.CharField(max_length=120, null=True, blank=True)
    facebook = models.CharField(max_length=120)
    instagram = models.CharField(max_length=120)
    twitter = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(max_length=50, default=' ')
    telefone = models.CharField(max_length=120)
    whatsapp = models.CharField(max_length=120, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('feira-detail',kwargs={'pid':self.id})
    def __str__(self):
        nome = str(self.id) + ' - ' + self.nome_feira
        return nome

class Organizadores(models.Model):
    funcao = models.CharField(max_length=120)
    facebook = models.CharField(max_length=120, null=True, blank=True)
    instagram = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    telefone = models.CharField(max_length=120, null=True, blank=True)
    whatsapp = models.CharField(max_length=120)
    usuario = models.OneToOneField(auth.models.User,on_delete=models.CASCADE)
    feira = models.ForeignKey(Feira,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('organizadores-detail',kwargs={'pid':self.id})

class Patrocinadores(models.Model):
    nome = models.CharField(max_length=120)
    link = models.CharField(max_length=300, null=True, blank=True)
    imagem_fundo = models.ImageField(upload_to="gestao_feira/logos/", null=True, blank=True)
    feira = models.ForeignKey(Feira,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('patrocinadores-detail',kwargs={'pid':self.id})

class Observacoes(models.Model):
    obs = models.TextField()
    feira = models.ForeignKey(Feira,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('observacoes-detail',kwargs={'pid':self.id})

class Instituicao(models.Model):
    razao_social = models.CharField(max_length=120)
    nome = models.CharField(max_length=120)
    cep = models.CharField(max_length=120)
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=120)
    bairro = models.CharField(max_length=120)
    endereco = models.CharField(max_length=120)

    def get_absolute_url(self):
        return reverse('instituicao-detail',kwargs={'pid':self.id})
