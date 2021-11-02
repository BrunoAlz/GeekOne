from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['NomeProduto', 'ProdutoSlug', 'PrecoProduto',
                    'EstoqueProduto', 'DataCriacao', 'DataModificacao', 'Ativo', ]
