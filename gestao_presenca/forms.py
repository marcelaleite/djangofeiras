from django import forms
from .models import Atividade,Inscricao

class AtividadeForm(forms.ModelForm):
		model = Atividade
		fields = [
		'titulo',
		'descricao',
		'carga_horaria',
		'palestrante'
		]

class AtividadeFormManual(forms.Form):
	titulo = models.CharField(max_length = 200)
	descricao = models.TextField()
	palestrante = models.ForeignKey(auth.models.User,on_delete=models.CASCADE)

class InscricaoForm(forms.ModelForm):
	class Meta:
		model = Inscricao
		fields = [
		'participou',
		'atividades',
		'usuario'
		]

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = [
        'nome',
        'sobrenome',
        'data_nascimento',
        'nacionalidade',
        'cpf',
        'rg',
        'telefone',
        'email',
        'instituicao',
        'formacao',
        'tipo',
        'cargo',
        'assinatura'
        ]
