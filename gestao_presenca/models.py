from django.db import models
from django.contrib import auth
from django.urls import reverse
from gestao_feira.models import Feira, Categoria

class Atividade(models.Model):
	titulo = models.CharField(max_length = 200)
	descricao = models.TextField()
	carga_horaria = models.DecimalField(decimal_places = 1, max_digits = 3, null = False, default = 0)
	palestrante = models.ForeignKey(auth.models.User,on_delete=models.CASCADE)
	def get_absolute_url(self):
		return reverse('atividade-detail',kwargs={'pid':self.id})
	def __str__(self):
		return str(self.id) + '-' +self.titulo+' - '+self.palestrante.get_full_name()

class Cronograma(models.Model):
        data = models.DateField()
        hora_inicio = models.TimeField()
        hora_fim = models.TimeField()
        local = models.CharField(max_length=120)
        hash = models.TextField(null = True, blank = True)
        feira = models.ForeignKey(Feira,on_delete=models.CASCADE)
        atividade = models.ForeignKey(Atividade,on_delete=models.CASCADE)

        def get_absolute_url(self):
                return reverse('gestao_presenca:cronograma-detail',kwargs={'pid':self.id})

        def get_url_qr_code(self):
                return reverse('gestao_presenca:atividade-qrcode',kwargs={'id_atividades':self.id})

class Inscricao(models.Model):
	data = models.DateField(auto_now_add = True)
	participou = models.BooleanField(default = False)
	cronograma = models.ForeignKey(Cronograma,on_delete=models.CASCADE)
	categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
	usuario = models.ForeignKey(auth.models.User,on_delete=models.CASCADE)
	def get_absolute_url(self):
		#return '/{self.id}/'
		return reverse('inscricao-detail',kwargs={'pid':self.id})

class Pessoa(models.Model):
        data_nascimento = models.DateField()
        nacionalidade = models.CharField(max_length=120)
        cpf = models.CharField(max_length=120)
        rg = models.CharField(max_length=120)
        telefone = models.CharField(max_length=120, null=True)
        email = models.EmailField(max_length=50)
        instituicao = models.CharField(max_length=120)
        formacao = models.CharField(max_length=120)
        #instituicao = models.ForeignKey(Instituicao,on_delete=models.CASCADE)
        usuario = models.OneToOneField(auth.models.User,on_delete=models.CASCADE)
        def get_absolute_url(self):
                return reverse('pessoa-detail',kwargs={'pid':self.id})
