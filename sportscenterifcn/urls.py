from django.urls import path

from sportscenterifcn import views

app_name = 'sportscenterifcn'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('noticias/', views.noticias, name='noticias'),
    path('arquivos/', views.arquivos, name='arquivos'),
    path('treinos/', views.treinos, name='treinos'),
    path('treinos/remover/<int:id>/', views.remover_treino, name='remover_treino'),
    path('treinos/adicionar/', views.adicionar_treino, name='adicionar_treino'),
    path('treinos/adicionar/salvar/', views.adicionar_treino_salvar, name='adicionar_treino_salvar'),
    path('treinos/editar/<int:id>/', views.editar_treino, name='editar_treino'),
    path('treinos/editar/<int:id>/salvar/', views.editar_treino_salvar, name='editar_treino_salvar'),
    path('historia/', views.historia, name='historia'),
    path('login/', views.login, name='login'),
    path('accounts/profile/', views.redirecionar_perfil, name='redirecionar_perfil'),
    path('perfil/', views.perfil, name='perfil'),
    path('logout/', views.logout, name='logout')
]
