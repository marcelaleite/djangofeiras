from django import forms
from .models import Atividade,Inscricao,Cronograma, Pessoa

class AtividadeForm(forms.ModelForm):
		model = Atividade
		fields = [
		'titulo',
		'descricao',
		'carga_horaria',
		'palestrante'
		]

#class AtividadeFormManual(forms.Form):
	#titulo = forms.CharField(max_length = '200')
	#descricao = forms.TextField()
	#palestrante = forms.ForeignKey(auth.models.User,on_delete=models.CASCADE)

class CronogramaForm(forms.ModelForm):
	class Meta:
		model = Cronograma
		fields = [
	    'data',
	    'hora_inicio',
	    'hora_fim',
	    'local',
	    'atividade',
	    'feira'
	    ]

class InscricaoForm(forms.ModelForm):
	class Meta:
		model = Inscricao
		fields = [
		'participou',
		'cronograma',
		'categoria',
		'usuario'
		]

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = [
        'data_nascimento',
        'nacionalidade',
        'cpf',
        'rg',
        'telefone',
        'email',
        'instituicao',
        'formacao'
		]
