# Generated by Django 4.2.8 on 2023-12-25 16:04

from django.db import migrations, models
import utils.noticia


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capa', models.ImageField(max_length=240, upload_to=utils.noticia.caminho_capa_noticia)),
                ('titulo', models.CharField(max_length=200)),
                ('excerto', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=220, unique=True)),
                ('conteudo', models.CharField(max_length=10000)),
                ('criada_em', models.DateTimeField(auto_now_add=True)),
                ('atualizada_em', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Treino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esporte', models.CharField(max_length=50)),
                ('dia_horario', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=70, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('matricula', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('nome_social', models.CharField(blank=True, max_length=50, null=True)),
                ('nome_registro', models.CharField(max_length=250)),
                ('primeiro_nome', models.CharField(max_length=50)),
                ('ultimo_nome', models.CharField(max_length=50)),
                ('email_pessoal', models.EmailField(max_length=250)),
                ('email_escolar', models.EmailField(max_length=250)),
                ('email_academico', models.EmailField(max_length=250)),
                ('campus', models.CharField(max_length=10)),
                ('foto', models.CharField(max_length=500)),
                ('tipo_usuario', models.CharField(max_length=30)),
                ('cpf', models.CharField(max_length=14)),
                ('data_nascimento', models.DateTimeField()),
                ('sexo', models.CharField(max_length=15)),
                ('permissao_administrador', models.BooleanField(default=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
