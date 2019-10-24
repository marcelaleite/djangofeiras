from django.db import models
from django.contrib import auth
from django.urls import reverse
from gestao_feira.models import Feiras

class Atividade(models.Model):
	titulo = models.CharField(max_length = 200)
	descricao = models.TextField()
	carga_horaria = models.DecimalField(decimal_places = 1, max_digits = 3, null = False, default = 0)
	palestrante = models.ForeignKey(auth.models.User,on_delete=models.CASCADE)
	feira = models.ForeignKey(Feira,on_delete=models.CASCADE)
	def get_absolute_url(self):
		return reverse('atividade-detail',kwargs={'pid':self.id})
	def __str__(self):
		return self.titulo+' - '+self.palestrante.get_full_name()

class Inscricao(models.Model):
	data = models.DateField(auto_now_add = True)
	participou = models.BooleanField(default = False)
	atividades = models.ForeignKey(Atividade,on_delete=models.CASCADE)
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
