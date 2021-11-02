from django import forms
from django.core.mail.message import EmailMessage
from utils.constants import CONSTANTES_ESTADOS, CONSTANTES_PAISES


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
    ContatoMensagem = forms.CharField(
        label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        ContatoPNome = self.cleaned_data['ContatoPNome']
        ContatoUNome = self.cleaned_data['ContatoUNome']
        ContatoUsername = self.cleaned_data['ContatoUsername']
        ContatoEmail = self.cleaned_data['ContatoEmail']
        ContatoEndereco1 = self.cleaned_data['ContatoEndereco1']
        ContatoPais = self.cleaned_data['ContatoPais']
        ContatoEstado = self.cleaned_data['ContatoEstado']
        ContatoCEP = self.cleaned_data['ContatoCEP']
        ContatoAssunto = self.cleaned_data['ContatoAssunto']
        ContatoMensagem = self.cleaned_data['ContatoMensagem']

        conteudo = f'Nome: {ContatoPNome} {ContatoUNome} \n{ContatoUsername} \n {ContatoEmail}'

        mail = EmailMessage(
            subject='Email testes',
            body=conteudo,
            from_email='contato@teste.com.br',
            to=['testeEmail@djangoTeste.com.br'],
            headers={'Reply-To': ContatoEmail}           
        )
        mail.send()