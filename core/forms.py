from django import forms
from utils.constants import BRASIL, CONSTANTES_ESTADOS, CONSTANTES_PAISES, SAO_PAULO

class ContatoForm(forms.Form):
    ContatoPNome = forms.CharField(max_length=50, label='Primeiro Nome')
    ContatoUNome = forms.CharField(max_length=70, label='Ultimo Nome')
    ContatoUsername = forms.CharField(max_length=30, label='Username')
    ContatoEmail = forms.EmailField(label='Email')
    ContatoEndereco1 = forms.CharField(max_length=400, label='Endereço')
    ContatoPais = forms.MultipleChoiceField(
        required=False,
        choices=CONSTANTES_PAISES,
        label='País'
    )
    ContatoEstado = forms.MultipleChoiceField(
        required=False,
        choices=CONSTANTES_ESTADOS,
        label='Estado'
    )
    ContatoCEP = forms.CharField(max_length=10, label='CEP')
    ContatoAssunto = forms.CharField(max_length=100, label='Assunto')
    ContatoMensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())