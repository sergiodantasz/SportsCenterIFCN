from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render
from django.urls import reverse

from sportscenterifcn import models


def inicio(request):
    contexto = {}
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        contexto.update({
            'usuario': usuario
        })
    return render(
        request,
        'sportscenterifcn/pages/inicio.html',
        contexto
    )


def noticias(request):
    contexto = {}
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        contexto.update({
            'usuario': usuario
        })
    return render(
        request,
        'sportscenterifcn/pages/noticias.html',
        contexto
    )


def arquivos(request):
    contexto = {}
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        contexto.update({
            'usuario': usuario
        })
    return render(
        request,
        'sportscenterifcn/pages/arquivos.html',
        contexto
    )


def treinos(request):
    contexto = {}
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        contexto.update({
            'usuario': usuario
        })
    treinos = models.Treino.objects.all()
    contexto.update({
        'treinos': treinos
    })
    return render(
        request,
        'sportscenterifcn/pages/treinos.html',
        contexto
    )


def remover_treino(request, id):
    treino = models.Treino.objects.get(id=id)
    treino.delete()
    return redirect(reverse('sportscenterifcn:treinos'))


def historia(request):
    contexto = {}
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        contexto.update({
            'usuario': usuario
        })
    return render(
        request,
        'sportscenterifcn/pages/historia.html',
        contexto
    )


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('sportscenterifcn:perfil'))
    return render(
        request,
        'sportscenterifcn/pages/login.html',
    )


def perfil(request):
    if not request.user.is_authenticated:
        return redirect(reverse('sportscenterifcn:login'))
    usuario = models.Usuario.objects.get(pk=request.user.username)
    return render(
        request,
        'sportscenterifcn/pages/perfil.html',
        {
            'usuario': usuario,
        }
    )


def redirecionar_perfil(request):
    return redirect(reverse('sportscenterifcn:perfil'))


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect(reverse('sportscenterifcn:inicio'))
