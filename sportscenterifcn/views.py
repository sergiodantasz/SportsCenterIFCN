from django.shortcuts import render


def inicio(request):
    return render(
        request,
        'sportscenterifcn/pages/inicio.html'
    )
