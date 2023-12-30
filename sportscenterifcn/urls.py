from django.shortcuts import redirect
from django.urls import reverse, path

from sportscenterifcn import views

app_name = 'sportscenterifcn'

urlpatterns = [
    # /
    path('', views.inicio, name='inicio'),

    # Notícias
    path('noticias/', views.noticias, name='noticias'),
    path('noticias/adicionar/', views.adicionar_noticia, name='adicionar_noticia'),
    path('noticias/adicionar/salvar/', views.adicionar_noticia_salvar, name='adicionar_noticia_salvar'),
    path('noticias/remover/<slug:slug>/', views.remover_noticia, name='remover_noticia'),
    path('noticias/editar/<slug:slug>/', views.editar_noticia, name='editar_noticia'),
    path('noticias/editar/<slug:slug>/salvar/', views.editar_noticia_salvar, name='editar_noticia_salvar'),
    path('noticias/visualizar/<slug:slug>/', views.visualizar_noticia, name='visualizar_noticia'),

    # Arquivos
    path('arquivos/', views.arquivos, name='arquivos'),
    path('arquivos/adicionar/', views.adicionar_arquivo, name='adicionar_arquivo'),
    path('arquivos/adicionar/salvar/', views.adicionar_arquivo_salvar, name='adicionar_arquivo_salvar'),
    path('arquivos/remover/<slug:slug>/', views.remover_arquivo, name='remover_arquivo'),
    path('arquivos/editar/<slug:slug>/', views.editar_arquivo, name='editar_arquivo'),
    path('arquivos/editar/<slug:slug>/salvar/', views.editar_arquivo_salvar, name='editar_arquivo_salvar'),
    path('arquivos/visualizar/<slug:slug>', views.visualizar_arquivo, name='visualizar_arquivo'),

    # Treinos
    path('treinos/', views.treinos, name='treinos'),
    path('treinos/adicionar/', views.adicionar_treino, name='adicionar_treino'),
    path('treinos/adicionar/salvar/', views.adicionar_treino_salvar, name='adicionar_treino_salvar'),
    path('treinos/remover/<slug:slug>/', views.remover_treino, name='remover_treino'),
    path('treinos/editar/<slug:slug>/', views.editar_treino, name='editar_treino'),
    path('treinos/editar/<slug:slug>/salvar/', views.editar_treino_salvar, name='editar_treino_salvar'),

    # História
    path('historia/', views.historia, name='historia'),

    # Perfil
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('accounts/profile/', lambda request: redirect(reverse('sportscenterifcn:perfil'))),
]
