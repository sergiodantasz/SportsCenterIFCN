from django.db import models

from utils.caminho import gerar_caminho_anexo_arquivo, gerar_caminho_capa
from utils.slug import gerar_slug_dinamica


class Usuario(models.Model):
    matricula = models.BigIntegerField(null=False, blank=False, primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    nome_social = models.CharField(max_length=250, null=True, blank=True, default=None)
    nome_registro = models.CharField(max_length=250, null=False, blank=False,)
    primeiro_nome = models.CharField(max_length=50, null=False, blank=False)
    ultimo_nome = models.CharField(max_length=50, null=False, blank=False)
    email_pessoal = models.EmailField(max_length=250, null=True, blank=False, default=None)
    email_escolar = models.EmailField(max_length=250, null=True, blank=False, default=None)
    email_academico = models.EmailField(max_length=250, null=True, blank=False, default=None)
    campus = models.CharField(max_length=10, null=False, blank=False)
    foto = models.URLField(max_length=500, null=False, blank=False)
    tipo_usuario = models.CharField(max_length=30, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    sexo = models.CharField(max_length=1, null=False, blank=False)


class Administrador(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, blank=False, db_column='matricula_usuario')


class Treino(models.Model):
    esporte = models.CharField(max_length=50, null=False, blank=False)
    dia_horario = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(max_length=70, unique=True)
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, null=False, blank=False, db_column='id_administrador')

    def save(self, *args, **kwargs):
        if not self.slug or self.esporte != Treino.objects.get(id=self.id).esporte:
            self.slug = gerar_slug_dinamica(self, 'esporte')
        return super().save(*args, **kwargs)


class Noticia(models.Model):
    capa = models.ImageField(max_length=240, upload_to=gerar_caminho_capa, null=False, blank=False)
    titulo = models.CharField(max_length=200, null=False, blank=False)
    excerto = models.CharField(max_length=300, null=False, blank=False)
    slug = models.SlugField(max_length=220, unique=True)
    conteudo = models.TextField(max_length=50000, null=False, blank=False)
    criada_em = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    atualizada_em = models.DateTimeField(auto_now=True, null=False, blank=False)
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, null=False, blank=False, db_column='id_administrador')

    def save(self, *args, **kwargs):
        if not self.slug or self.titulo != Noticia.objects.get(id=self.id).titulo:
            self.slug = gerar_slug_dinamica(self, 'titulo')
        return super().save(*args, **kwargs)


class Arquivo(models.Model):
    capa = models.ImageField(max_length=240, upload_to=gerar_caminho_capa, null=False, blank=False)
    titulo = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=220, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    atualizado_em = models.DateTimeField(auto_now=True, null=False, blank=False)
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, null=False, blank=False, db_column='id_administrador')

    def save(self, *args, **kwargs):
        if not self.slug or self.titulo != Arquivo.objects.get(id=self.id).titulo:
            self.slug = gerar_slug_dinamica(self, 'titulo')
        return super().save(*args, **kwargs)


class AnexoArquivo(models.Model):
    arquivo = models.ForeignKey(Arquivo, on_delete=models.CASCADE, null=False, blank=False, db_column='id_arquivo')
    anexo = models.ImageField(max_length=240, upload_to=gerar_caminho_anexo_arquivo, null=False, blank=False)
