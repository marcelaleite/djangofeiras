from django import forms
from .models import Feira, Cronograma, Organizadores, Patrocinadores,
 Observacoes, Pessoa

 class FeiraForm(forms.ModelForm):
    class Meta:
        model = Feira
		fields = [
		'nome_feira',
		'area',
		'data_inicio',
        'data_fim',
        'hora_inicio',
        'hora_fim',
        'cep',
        'uf',
        'cidade',
        'bairro',
        'endereco',
        'complemento',
        'facebook',
        'instagram',
        'twitter',
        'email',
        'telefone',
        'whatsapp'
		]

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

class OrganizadoresForm(forms.ModelForm):
    class Meta:
        model = Organizadores
        fields = [
        'funcao',
        'facebook',
        'instagram',
        'email',
        'telefone',
        'whatsapp',
        'pessoa',
        'feira'
        ]

class PatrocinadoresForm(forms.ModelForm):
    class Meta:
        model = Patrocinadores
        fields = [
        'nome',
        'link',
        'imagem_fundo',
        'feira'
        ]

class ObservacoesForm(forms.ModelForm):
    class Meta:
        model = Observacoes
        fields = [
        'obs',
        'feira'
        ]

class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = Observacoes
        fields = [
        'razao_social',
        'nome',
        'cep',
        'uf',
        'cidade',
        'bairro',
        'endereco'
        ]
