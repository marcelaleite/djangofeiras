from django import forms

from gestao_feira.models import Feira, Categoria

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

    feira = forms.ModelChoiceField(queryset=Feira.objects.all(),
                                   label='Feira Aplicável ao Certificado',
                                   required=True)

    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(),
                                       label='Categoria Aplicável de Certificação',
                                       required=True)

    class Meta:
        model = Certificado
        fields = [
            'nome_modelo',
            'feira',
            'categoria',
            'ptext',
            'imagem_fundo',
            'imagem_evento'
        ]
