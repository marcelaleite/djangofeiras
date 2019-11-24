from django import forms

from gestao_feira.models import Categoria

from .models import Certificado

class CertificadoForm(forms.ModelForm):
    nome_modelo = forms.CharField(label='Nome do Modelo',
                                  max_length=50,
                                  required=True,
                                  widget=forms.Textarea(attrs={'placeholder':'Informe um nome para o modelo de certificado...',
                                                               'id':'nome-modelo',
                                                               'class':'campos',
                                                               'cols':89,
                                                               'rows':1}))

    ptext = forms.CharField(label='Paragrafo de Descrição',
                            max_length=500,
                            required=True,
                            widget=forms.Textarea(attrs={'placeholder':'Informe o paragrafo para a descrição do certificado...',
                                                         'id':'ptext',
                                                         'class':'campos',
                                                         'cols':89,
                                                         'rows':5}))

    imagem_fundo = forms.ImageField(label='Imagem de Fundo',
                                    required=False)

    imagem_evento = forms.ImageField(label='Imagem do Evento',
                                     required=False)

    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(),
                                       label='Categoria Aplicável de Certificação',
                                       required=True)

    class Meta:
        model = Certificado
        fields = [
            'nome_modelo',
            'categoria',
            'ptext',
            'imagem_fundo',
            'imagem_evento'
        ]

class CertificadoFormManual(forms.Form):
    nome = forms.CharField(max_length='120')
    sobrenome = forms.CharField(max_length='120')

    def clean_nome(self, *args, **kwargs):
        nome = self.cleaned_data.get('nome')
        if not 'de' in nome:
            raise forms.ValidationError('Nome não compativel com o padrão')
        return nome
