from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
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
    return render(
        request,
        'sportscenterifcn/pages/treinos.html',
        contexto
    )


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
        return HttpResponseRedirect(reverse('sportscenterifcn:perfil'))
    return render(
        request,
        'sportscenterifcn/pages/login.html',
    )


def perfil(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('sportscenterifcn:login'))
    usuario = models.Usuario.objects.get(pk=request.user.username)
    return render(
        request,
        'sportscenterifcn/pages/perfil.html',
        {
            'usuario': usuario,
        }
    )


def redirecionar_perfil(request):
    return HttpResponseRedirect(reverse('sportscenterifcn:perfil'))


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return HttpResponseRedirect(reverse('sportscenterifcn:inicio'))
