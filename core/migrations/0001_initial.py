# Generated by Django 3.2.8 on 2021-11-02 12:31

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DataCriacao', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('DataModificacao', models.DateField(auto_now_add=True, verbose_name='Data de Atualização')),
                ('Ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('NomeProduto', models.CharField(max_length=150, verbose_name='Descrição')),
                ('PrecoProduto', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Descrição')),
                ('EstoqueProduto', models.IntegerField(verbose_name='Estoque')),
                ('ProdutoImage', stdimage.models.StdImageField(upload_to='produtos', verbose_name='Image')),
                ('ProdutoSlug', models.SlugField(blank=True, editable=False, max_length=150, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
