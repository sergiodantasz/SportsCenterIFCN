from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def inicio(request):
    return render(
        request,
        'sportscenterifcn/pages/inicio.html',
    )


def noticias(request):
    return render(
        request,
        'sportscenterifcn/pages/noticias.html',
    )


def arquivos(request):
    return render(
        request,
        'sportscenterifcn/pages/arquivos.html',
    )


def treinos(request):
    return render(
        request,
        'sportscenterifcn/pages/treinos.html',
    )


def historia(request):
    return render(
        request,
        'sportscenterifcn/pages/historia.html',
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
    return render(
        request,
        'sportscenterifcn/pages/perfil.html',
    )


def redirecionar_perfil(request):
    return HttpResponseRedirect(reverse('sportscenterifcn:perfil'))


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return HttpResponseRedirect(reverse('sportscenterifcn:inicio'))
