from django.db import models
from stdimage.models import StdImageField

#
from django.db.models import signals
# o Slugify Pega dados e transforma em urls.
from django.template.defaultfilters import default, slugify


class Base(models.Model):
    """ A classe BASE é uma class abstrata e não é criada no banco de addos
    servirá apenas de rascunho para outras classes. """
    DataCriacao = models.DateField('Data de Criação', auto_now_add=True)
    DataModificacao = models.DateField(
        'Data de Atualização', auto_now_add=True)
    Ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Produto(Base):
    NomeProduto = models.CharField(max_length=150, verbose_name='Descrição')
    PrecoProduto = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='Preço')
    EstoqueProduto = models.IntegerField(verbose_name='Estoque')
    ProdutoImage = StdImageField(
        'Image', upload_to='produtos', variations={'thumb': (124, 124)})
    ProdutoSlug = models.SlugField(
        max_length=150, blank=True, editable=False, verbose_name='Slug')

    def __str__(self) -> str:
        return self.NomeProduto


"""A função produto_pre_save Envia um sinal para que quando Produto for ser salvo no banco
ele pega o nome do produto em instance.NomeProduto passa na função Slugify para
transformar em slug e depois manda para a variável instance.ProdutoSlug"""


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.ProdutoSlug = slugify(instance.NomeProduto)


signals.pre_save.connect(produto_pre_save, sender=Produto)
