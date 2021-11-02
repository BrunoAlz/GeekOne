from django.shortcuts import redirect, render
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages
from .models import Produto
from django.shortcuts import redirect


def index(request):
    context = {
        'produtos' : Produto.objects.all()
    }    
    return render(request, 'core/index.html', context)


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
    if str(request.user) != 'AnonymousUser': # Verifica se o usuário está logado
        if str(request.method) == 'POST':  # Verifica se o request é do tipo POST
            # Recupera os dados do HTML
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():  # Verifica se tudo foi preenchido

                form.save()

                messages.success(request, 'Produto Salvo Sucesso!')
                form = ProdutoModelForm()  # Limpa o FORM
            else:
                messages.error(request, 'Erro ao Salvar')
        else:
            form = ProdutoModelForm()

        context = {
            'form': form
        }
        return render(request, 'core/produto.html', context)
    else:
        return redirect('index')
