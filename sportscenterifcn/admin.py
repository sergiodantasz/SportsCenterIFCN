from django.contrib import admin

from sportscenterifcn import models


@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Treino)
class TreinoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Arquivo)
class ArquivoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AnexoArquivo)
class AnexoArquivoAdmin(admin.ModelAdmin):
    pass
