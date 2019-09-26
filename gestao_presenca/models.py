from django.db import models
from django.contrib import auth
from django.urls import reverse

class Atividade(models.Model):
	titulo = models.CharField(max_length = 200)
	descricao = models.TextField()
	palestrante = models.ForeignKey(auth.models.User,on_delete=models.CASCADE)
	def get_absolute_url(self):
		return reverse('atividade-detail',kwargs={'pid':self.id})
	
class Inscricao(models.Model):
	data = models.DateField(auto_now_add = True)
	atividades = models.ForeignKey(Atividade,on_delete=models.CASCADE)
	usuario = models.ForeignKey(auth.models.User,on_delete=models.CASCADE)
	def get_absolute_url(self):
		#return '/{self.id}/'
		return reverse('inscricao-detail',kwargs={'pid':self.id})

