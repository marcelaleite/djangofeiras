from django.db import models
from django.contrib import auth
from django.urls import reverse

class Atividade(models.Model):
	titulo = models.CharField(max_length = 200)
	descricao = models.TextField()
	carga_horaria = models.IntegerField(null = False)
	palestrante = models.ForeignKey(auth.models.User,on_delete=models.CASCADE)
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

