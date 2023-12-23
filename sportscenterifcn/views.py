from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render
from django.urls import reverse

from sportscenterifcn import forms, models


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
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        if usuario.permissao_administrador != 1:
            return redirect(reverse('sportscenterifcn:treinos'))
    treino = models.Treino.objects.get(id=id)
    treino.delete()
    return redirect(reverse('sportscenterifcn:treinos'))


def adicionar_treino(request):
    contexto = {}
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        if usuario.permissao_administrador != 1:
            return redirect(reverse('sportscenterifcn:treinos'))
        contexto.update({
            'usuario': usuario
        })
    form = forms.TreinoForm()
    contexto.update({
        'form': form,
        'form_action': reverse('sportscenterifcn:adicionar_treino_salvar')
    })
    return render(
        request,
        'sportscenterifcn/pages/adicionar-treino.html',
        contexto
    )


def adicionar_treino_salvar(request):
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        if usuario.permissao_administrador != 1:
            return redirect(reverse('sportscenterifcn:treinos'))
    form = forms.TreinoForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        # TODO: Inserir mensagens de erro na página.
        pass
    return redirect(reverse('sportscenterifcn:treinos'))


def editar_treino(request, id):
    contexto = {}
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        if usuario.permissao_administrador != 1:
            return redirect(reverse('sportscenterifcn:treinos'))
        contexto.update({
            'usuario': usuario
        })
    treino = models.Treino.objects.get(id=id)
    form = forms.TreinoForm(instance=treino)
    contexto.update({
        'form': form,
        'form_action': reverse(
            'sportscenterifcn:editar_treino_salvar', kwargs={'id': id}
        ),
    })
    return render(
        request,
        'sportscenterifcn/pages/editar-treino.html',
        contexto
    )


def editar_treino_salvar(request, id):
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        if usuario.permissao_administrador != 1:
            return redirect(reverse('sportscenterifcn:treinos'))
    treino = models.Treino.objects.get(id=id)
    form = forms.TreinoForm(request.POST, instance=treino)
    if form.is_valid():
        form.save()
    else:
        # TODO: Inserir mensagens de erro na página.
        pass
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
