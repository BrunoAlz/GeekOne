from django.shortcuts import render
from .forms import ContatoForm


def index(request):
    return render(request, 'core/index.html')


def contato(request):
    form = ContatoForm()  # form recebe uma Instancia do Nosso formulário

    context = {
        'form': form
    }
    return render(request, 'core/contato.html', context)


def produto(request):
    return render(request, 'core/produto.html')
