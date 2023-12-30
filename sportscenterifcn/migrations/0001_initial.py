# Generated by Django 4.2.8 on 2023-12-30 22:53

from django.db import migrations, models
import django.db.models.deletion
import utils.caminho


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('matricula', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('nome_social', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('nome_registro', models.CharField(max_length=250)),
                ('primeiro_nome', models.CharField(max_length=50)),
                ('ultimo_nome', models.CharField(max_length=50)),
                ('email_pessoal', models.EmailField(default=None, max_length=250, null=True)),
                ('email_escolar', models.EmailField(default=None, max_length=250, null=True)),
                ('email_academico', models.EmailField(default=None, max_length=250, null=True)),
                ('campus', models.CharField(max_length=10)),
                ('foto', models.URLField(max_length=500)),
                ('tipo_usuario', models.CharField(max_length=30)),
                ('cpf', models.CharField(max_length=14)),
                ('data_nascimento', models.DateField()),
                ('sexo', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Treino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esporte', models.CharField(max_length=50)),
                ('dia_horario', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=70, unique=True)),
                ('administrador', models.ForeignKey(db_column='id_administrador', null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportscenterifcn.administrador')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capa', models.ImageField(max_length=240, upload_to=utils.caminho.gerar_caminho_capa)),
                ('titulo', models.CharField(max_length=200)),
                ('excerto', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=220, unique=True)),
                ('conteudo', models.TextField(max_length=50000)),
                ('criada_em', models.DateTimeField(auto_now_add=True)),
                ('atualizada_em', models.DateTimeField(auto_now=True)),
                ('administrador', models.ForeignKey(db_column='id_administrador', null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportscenterifcn.administrador')),
            ],
        ),
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capa', models.ImageField(max_length=240, upload_to='')),
                ('titulo', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=220, unique=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('administrador', models.ForeignKey(db_column='id_administrador', null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportscenterifcn.administrador')),
            ],
        ),
        migrations.CreateModel(
            name='AnexoArquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anexo', models.ImageField(max_length=240, upload_to=utils.caminho.gerar_caminho_anexo_arquivo)),
                ('arquivo', models.ForeignKey(db_column='id_arquivo', on_delete=django.db.models.deletion.CASCADE, to='sportscenterifcn.arquivo')),
            ],
        ),
        migrations.AddField(
            model_name='administrador',
            name='usuario',
            field=models.ForeignKey(db_column='matricula_usuario', on_delete=django.db.models.deletion.CASCADE, to='sportscenterifcn.usuario'),
        ),
    ]
