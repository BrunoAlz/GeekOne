from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages


def index(request):
    return render(request, 'core/index.html')


def contato(request):
    # form recebe uma Instancia do Nosso formulário
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()            
            messages.success(request, 'Contanto realizado com Sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar sua mensagem.')

    context = {
        'form': form
    }
    return render(request, 'core/contato.html', context)


def produto(request):
    return render(request, 'core/produto.html')
