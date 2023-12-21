from django.urls import path

from sportscenterifcn import views

app_name = 'sportscenterifcn'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('noticias/', views.noticias, name='noticias'),
    path('arquivos/', views.arquivos, name='arquivos'),
    path('treinos/', views.treinos, name='treinos'),
    path('treinos/remover/<int:id>/', views.remover_treino, name='remover_treino'),
    path('historia/', views.historia, name='historia'),
    path('login/', views.login, name='login'),
    path('accounts/profile/', views.redirecionar_perfil, name='redirecionar_perfil'),
    path('perfil/', views.perfil, name='perfil'),
    path('logout/', views.logout, name='logout')
]
