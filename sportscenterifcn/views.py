from django.contrib.auth import logout as auth_logout
from django.shortcuts import get_object_or_404, get_list_or_404, redirect, render
from django.urls import reverse

from sportscenterifcn import forms, models
from utils.paginacao import criar_paginacao


# INÍCIO

def inicio(request):
    noticias = models.Noticia.objects.all().order_by('-id')[:3]
    contexto = {
        'noticias': noticias
    }
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


# NOTÍCIAS

def noticias(request):
    contexto = {}
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        contexto.update({
            'usuario': usuario,
            'administrador': None
        })
        administrador = models.Administrador.objects.filter(usuario=usuario.matricula)
        if administrador.count() == 1:
            contexto.update({
                'administrador': administrador[0]
            })
    noticias = models.Noticia.objects.all().order_by('-id')
    page_obj, pagination_range = criar_paginacao(request, noticias, 5)
    contexto.update({
        'noticias': page_obj,
        'pagination_range': pagination_range
    })
    return render(
        request,
        'sportscenterifcn/pages/noticias.html',
        contexto
    )


def visualizar_noticia(request, slug):
    contexto = {}
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        contexto.update({
            'usuario': usuario,
            'administrador': None
        })
        administrador = models.Administrador.objects.filter(usuario=usuario.matricula)
        if administrador.count() == 1:
            contexto.update({
                'administrador': administrador[0]
            })
    noticia = get_object_or_404(models.Noticia, slug=slug)
    contexto.update({
        'noticia': noticia
    })
    return render(
        request,
        'sportscenterifcn/pages/visualizar-noticia.html',
        contexto
    )


def adicionar_noticia(request):
    contexto = {}
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        contexto.update({
            'usuario': usuario
        })
        administrador = models.Administrador.objects.filter(usuario=usuario.matricula)
        if administrador.count() != 1:
            return redirect(reverse('sportscenterifcn:noticias'))
    dados_formulario = request.session.get('dados_formulario')
    form = forms.NoticiaForm(dados_formulario)
    contexto.update({
        'form': form,
        'form_action': reverse('sportscenterifcn:adicionar_noticia_salvar')
    })
    return render(
        request,
        'sportscenterifcn/pages/adicionar-noticia.html',
        contexto
    )


def adicionar_noticia_salvar(request):
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        administrador = models.Administrador.objects.filter(usuario=usuario.matricula)
        if administrador.count() != 1:
            return redirect(reverse('sportscenterifcn:noticias'))
        administrador = administrador[0]
    request.session['dados_formulario'] = request.POST
    form = forms.NoticiaForm(request.POST, request.FILES)
    if form.is_valid():
        del(request.session['dados_formulario'])
        noticia = form.save()
        noticia.administrador = administrador
        noticia.save()
    else:
        return redirect(reverse('sportscenterifcn:adicionar_noticia'))
    return redirect(reverse('sportscenterifcn:noticias'))


def editar_noticia(request, slug):
    contexto = {}
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        contexto.update({
            'usuario': usuario
        })
        administrador = models.Administrador.objects.filter(usuario=usuario.matricula)
        if administrador.count() != 1:
            return redirect(reverse('sportscenterifcn:visualizar_noticia', kwargs={'slug': slug}))
    dados_formulario = request.session.get('dados_formulario')
    noticia = get_object_or_404(models.Noticia, slug=slug)
    form = forms.NoticiaForm(dados_formulario, instance=noticia)
    contexto.update({
        'form': form,
        'form_action': reverse(
            'sportscenterifcn:editar_noticia_salvar', kwargs={'slug': slug}
        ),
        'noticia': noticia,
    })
    return render(
        request,
        'sportscenterifcn/pages/editar-noticia.html',
        contexto
    )


def editar_noticia_salvar(request, slug):
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        administrador = models.Administrador.objects.filter(usuario=usuario.matricula)
        if administrador.count() != 1:
            return redirect(reverse('sportscenterifcn:visualizar_noticia', kwargs={'slug': slug}))
    request.session['dados_formulario'] = request.POST
    noticia = get_object_or_404(models.Noticia, slug=slug)
    form = forms.NoticiaForm(request.POST, request.FILES, instance=noticia)
    if form.is_valid():
        del(request.session['dados_formulario'])
        form.save()
    return redirect(reverse('sportscenterifcn:visualizar_noticia', kwargs={'slug': noticia.slug}))


def remover_noticia(request, slug):
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        administrador = models.Administrador.objects.filter(usuario=usuario.matricula)
        if administrador.count() != 1:
            return redirect(reverse('sportscenterifcn:noticias'))
    noticia = get_object_or_404(models.Noticia, slug=slug)
    noticia.delete()
    return redirect(reverse('sportscenterifcn:noticias'))


# ARQUIVOS

def arquivos(request):
    contexto = {}
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        contexto.update({
            'usuario': usuario,
            'administrador': None
        })
        administrador = models.Administrador.objects.filter(usuario=usuario.matricula)
        if administrador.count() == 1:
            contexto.update({
                'administrador': administrador[0]
            })
    arquivos = models.Arquivo.objects.all().order_by('-id')
    page_obj, pagination_range = criar_paginacao(request, arquivos, 12)
    contexto.update({
        'arquivos': page_obj,
        'pagination_range': pagination_range
    })
    return render(
        request,
        'sportscenterifcn/pages/arquivos.html',
        contexto
    )


def adicionar_arquivo(request):
    contexto = {}
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        contexto.update({
            'usuario': usuario
        })
        administrador = models.Administrador.objects.filter(usuario=usuario.matricula)
        if administrador.count() != 1:
            return redirect(reverse('sportscenterifcn:arquivos'))
    dados_formulario = request.session.get('dados_formulario')
    form_arquivo = forms.ArquivoForm(dados_formulario)
    form_anexo = forms.AnexoArquivoForm(dados_formulario)
    contexto.update({
        'form_arquivo': form_arquivo,
        'form_anexo': form_anexo,
        'form_action': reverse('sportscenterifcn:adicionar_arquivo_salvar')
    })
    return render(
        request,
        'sportscenterifcn/pages/adicionar-arquivo.html',
        contexto
    )


def adicionar_arquivo_salvar(request):
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        administrador = models.Administrador.objects.filter(usuario=usuario.matricula)
        if administrador.count() != 1:
            return redirect(reverse('sportscenterifcn:arquivos'))
        administrador = administrador[0]
    request.session['dados_formulario'] = request.POST
    form_arquivo = forms.ArquivoForm(request.POST)
    imagens = request.FILES.getlist('anexo')
    if form_arquivo.is_valid():
        del(request.session['dados_formulario'])
        arquivo = form_arquivo.save()
        for i, imagem in enumerate(imagens):
            img = models.AnexoArquivo.objects.create(
                arquivo=arquivo,
                anexo=imagem
            )
            if i == 0:
                arquivo.capa = img.anexo
                arquivo.save()
        arquivo.administrador = administrador
        arquivo.save()
    return redirect(reverse('sportscenterifcn:arquivos'))


def editar_arquivo(request, slug):
    contexto = {}
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        contexto.update({
            'usuario': usuario
        })
        administrador = models.Administrador.objects.filter(usuario=usuario.matricula)
        if administrador.count() != 1:
            return redirect(reverse('sportscenterifcn:visualizar_arquivo', kwargs={'slug': slug}))
    dados_formulario = request.session.get('dados_formulario')
    arquivo = get_object_or_404(models.Arquivo, slug=slug)
    form_arquivo = forms.ArquivoForm(dados_formulario, instance=arquivo)
    imagens = get_list_or_404(models.AnexoArquivo.objects.order_by('id'), arquivo=arquivo.id)
    form_anexo = forms.AnexoArquivoForm(dados_formulario)
    form_anexo.fields['anexo'].required = False
    contexto.update({
        'form_arquivo': form_arquivo,
        'form_anexo': form_anexo,
        'imagens': imagens,
        'form_action': reverse(
            'sportscenterifcn:editar_arquivo_salvar', kwargs={'slug': slug}
        ),
        'arquivo': arquivo,
    })
    return render(
        request,
        'sportscenterifcn/pages/editar-arquivo.html',
        contexto
    )


def editar_arquivo_salvar(request, slug):
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        administrador = models.Administrador.objects.filter(usuario=usuario.matricula)
        if administrador.count() != 1:
            return redirect(reverse('sportscenterifcn:visualizar_arquivo', kwargs={'slug': slug}))
    request.session['dados_formulario'] = request.POST
    id_imagens_removidas = []
    for k, v in request.POST.items():
        if 'imagem' in k and v == 'on':
            id_imagem = k.split('-')[1]
            id_imagens_removidas.append(int(id_imagem))
    arquivo = get_object_or_404(models.Arquivo, slug=slug)
    form_arquivo = forms.ArquivoForm(request.POST, request.FILES, instance=arquivo)
    imagens = models.AnexoArquivo.objects.filter(arquivo=arquivo.id).order_by('id')
    if form_arquivo.is_valid():
        del(request.session['dados_formulario'])
        arquivo = form_arquivo.save()
        imagens_adicionadas = request.FILES.getlist('anexo')
        for imagem in imagens_adicionadas:
            models.AnexoArquivo.objects.create(
                arquivo=arquivo,
                anexo=imagem
            )
        imagens_nao_removidas = [
            imagem for imagem in imagens if imagem.id not in id_imagens_removidas
        ]
        if len(imagens_nao_removidas) == 0 and len(imagens_adicionadas) == 0:
            arquivo.delete()
            return redirect(reverse('sportscenterifcn:arquivos'))
        if len(imagens_nao_removidas) > 0:
            for id_imagem in id_imagens_removidas:
                imagem = imagens.get(id=id_imagem)
                if imagem.anexo.url == arquivo.capa.url:
                    nova_capa = imagens_nao_removidas[0]
                    arquivo.capa = nova_capa.anexo
                    arquivo.save()
                imagem.delete()
        elif len(imagens_adicionadas) > 0:
                nova_capa = imagens_adicionadas[0]
                arquivo.capa = nova_capa.anexo
                arquivo.save()
    return redirect(reverse('sportscenterifcn:visualizar_arquivo', kwargs={'slug': arquivo.slug}))


def remover_arquivo(request, slug):
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        administrador = models.Administrador.objects.filter(usuario=usuario.matricula)
        if administrador.count() != 1:
            return redirect(reverse('sportscenterifcn:arquivos'))
    arquivo = get_object_or_404(models.Arquivo, slug=slug)
    arquivo.delete()
    return redirect(reverse('sportscenterifcn:arquivos'))


def visualizar_arquivo(request, slug):
    contexto = {}
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        contexto.update({
            'usuario': usuario,
            'administrador': None
        })
        administrador = models.Administrador.objects.filter(usuario=usuario.matricula)
        if administrador.count() == 1:
            contexto.update({
                'administrador': administrador[0]
            })
    arquivo = get_object_or_404(models.Arquivo, slug=slug)
    imagens = get_list_or_404(models.AnexoArquivo.objects.order_by('id'), arquivo=arquivo.id)
    contexto.update({
        'arquivo': arquivo,
        'imagens': imagens
    })
    return render(
        request,
        'sportscenterifcn/pages/visualizar-arquivo.html',
        contexto
    )


# TREINOS

def treinos(request):
    contexto = {}
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        contexto.update({
            'usuario': usuario,
            'administrador': None
        })
        administrador = models.Administrador.objects.filter(usuario=usuario.matricula)
        if administrador.count() == 1:
            contexto.update({
                'administrador': administrador[0]
            })
    treinos = models.Treino.objects.all().order_by('esporte')
    contexto.update({
        'treinos': treinos
    })
    return render(
        request,
        'sportscenterifcn/pages/treinos.html',
        contexto
    )


def remover_treino(request, slug):
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        administrador = models.Administrador.objects.filter(usuario=usuario.matricula)
        if administrador.count() != 1:
            return redirect(reverse('sportscenterifcn:treinos'))
    treino = get_object_or_404(models.Treino, slug=slug)
    treino.delete()
    return redirect(reverse('sportscenterifcn:treinos'))


def adicionar_treino(request):
    contexto = {}
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        contexto.update({
            'usuario': usuario
        })
        administrador = models.Administrador.objects.filter(usuario=usuario.matricula)
        if administrador.count() != 1:
            return redirect(reverse('sportscenterifcn:treinos'))
    dados_formulario = request.session.get('dados_formulario')
    form = forms.TreinoForm(dados_formulario)
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
        administrador = models.Administrador.objects.filter(usuario=usuario.matricula)
        if administrador.count() != 1:
            return redirect(reverse('sportscenterifcn:treinos'))
        administrador = administrador[0]
    request.session['dados_formulario'] = request.POST
    form = forms.TreinoForm(request.POST)
    if form.is_valid():
        del(request.session['dados_formulario'])
        treino = form.save()
        treino.administrador = administrador
        treino.save()
    return redirect(reverse('sportscenterifcn:treinos'))


def editar_treino(request, slug):
    contexto = {}
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        contexto.update({
            'usuario': usuario
        })
        administrador = models.Administrador.objects.filter(usuario=usuario.matricula)
        if administrador.count() != 1:
            return redirect(reverse('sportscenterifcn:treinos', kwargs={'slug': slug}))
    dados_formulario = request.session.get('dados_formulario')
    treino = get_object_or_404(models.Treino, slug=slug)
    form = forms.TreinoForm(dados_formulario, instance=treino)
    contexto.update({
        'form': form,
        'form_action': reverse(
            'sportscenterifcn:editar_treino_salvar', kwargs={'slug': slug}
        ),
        'treino': treino
    })
    return render(
        request,
        'sportscenterifcn/pages/editar-treino.html',
        contexto
    )


def editar_treino_salvar(request, slug):
    if request.user.is_authenticated:
        usuario = models.Usuario.objects.get(pk=request.user.username)
        administrador = models.Administrador.objects.filter(usuario=usuario.matricula)
        if administrador.count() != 1:
            return redirect(reverse('sportscenterifcn:treinos', kwargs={'slug': slug}))
    request.session['dados_formulario'] = request.POST
    treino = get_object_or_404(models.Treino, slug=slug)
    form = forms.TreinoForm(request.POST, instance=treino)
    if form.is_valid():
        del(request.session['dados_formulario'])
        form.save()
    return redirect(reverse('sportscenterifcn:treinos'))


# HISTÓRIA

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


# PERFIL

def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('sportscenterifcn:perfil'))
    return render(
        request,
        'sportscenterifcn/pages/login.html',
    )


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect(reverse('sportscenterifcn:inicio'))


def perfil(request):
    if not request.user.is_authenticated:
        return redirect(reverse('sportscenterifcn:login'))
    usuario = models.Usuario.objects.get(pk=request.user.username)
    emails = []
    if usuario.email_pessoal:
        emails.append(usuario.email_pessoal)
    if usuario.email_escolar:
        emails.append(usuario.email_escolar)
    if usuario.email_academico:
        emails.append(usuario.email_academico)
    return render(
        request,
        'sportscenterifcn/pages/perfil.html',
        {
            'usuario': usuario,
            'emails': emails
        }
    )
