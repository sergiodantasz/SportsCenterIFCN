from django.shortcuts import render


def inicio(request):
    return render(
        request,
        'sportscenterifcn/pages/inicio.html'
    )


def noticias(request):
    return render(
        request,
        'sportscenterifcn/pages/noticias.html'
    )


def arquivos(request):
    return render(
        request,
        'sportscenterifcn/pages/arquivos.html'
    )


def treinos(request):
    return render(
        request,
        'sportscenterifcn/pages/treinos.html'
    )


def historia(request):
    return render(
        request,
        'sportscenterifcn/pages/historia.html'
    )


def login(request):
    return render(
        request,
        'sportscenterifcn/pages/login.html'
    )
