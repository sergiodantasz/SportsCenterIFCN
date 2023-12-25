from os import rename
from os.path import split, splitext

from django.db import models

from utils.noticia import caminho_capa_noticia
from utils.slug import gerar_slug_dinamica


class Usuario(models.Model):
    matricula = models.CharField(max_length=14, null=False, blank=False, primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    nome_social = models.CharField(max_length=50, null=True, blank=True)
    nome_registro = models.CharField(max_length=250, null=False, blank=False,)
    primeiro_nome = models.CharField(max_length=50, null=False, blank=False)
    ultimo_nome = models.CharField(max_length=50, null=False, blank=False)
    email_pessoal = models.EmailField(max_length=250, null=False, blank=False)
    email_escolar = models.EmailField(max_length=250, null=False, blank=False)
    email_academico = models.EmailField(max_length=250, null=False, blank=False)
    campus = models.CharField(max_length=10, null=False, blank=False)
    foto = models.CharField(max_length=500, null=False, blank=False)
    tipo_usuario = models.CharField(max_length=30, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    data_nascimento = models.DateTimeField(null=False, blank=False)
    sexo = models.CharField(max_length=15, null=False, blank=False)
    permissao_administrador = models.BooleanField(null=False, blank=False, default=False)
    criado_em = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    atualizado_em = models.DateTimeField(auto_now=True, null=False, blank=False)


class Treino(models.Model):
    esporte = models.CharField(max_length=50, null=False, blank=False)
    dia_horario = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(max_length=70, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug or self.esporte != Treino.objects.get(id=self.id).esporte:
            self.slug = gerar_slug_dinamica(self, 'esporte')
        return super().save(*args, **kwargs)


class Noticia(models.Model):
    capa = models.ImageField(max_length=240, upload_to=caminho_capa_noticia, null=False, blank=False)
    titulo = models.CharField(max_length=200, null=False, blank=False)
    excerto = models.CharField(max_length=300, null=False, blank=False)
    slug = models.SlugField(max_length=220, unique=True)
    conteudo = models.CharField(max_length=10000, null=False, blank=False)
    criada_em = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    atualizada_em = models.DateTimeField(auto_now=True, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.slug or self.titulo != Noticia.objects.get(id=self.id).titulo:
            self.slug = gerar_slug_dinamica(self, 'titulo')
        caminho, arquivo = split(self.capa.name)
        arquivo, ext = splitext(arquivo)
        if self.id and arquivo != self.slug:
            arquivo_antigo = self.capa.path
            self.capa.name = caminho_capa_noticia(self, self.slug + ext)
            rename(arquivo_antigo, self.capa.path)
        return super().save(*args, **kwargs)
