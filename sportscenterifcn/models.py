from django.db import models


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
    dia_horario = models.CharField(max_length=100, null=False, blank=False)
