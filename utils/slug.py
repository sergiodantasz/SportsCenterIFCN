from random import SystemRandom
from string import ascii_letters, digits

from django.utils.text import slugify


def gerar_letras_aleatorias(k: int = 5):
    return ''.join(
        SystemRandom().choices(ascii_letters + digits, k=k)
    )


def gerar_slug(string: str, k: int = 5):
    if k == 0:
        return slugify(string)
    return slugify(string) + '-' + gerar_letras_aleatorias(k)


def gerar_slug_dinamica(instancia, campo):
    model = instancia.__class__
    valor_campo = getattr(instancia, campo)
    slug = gerar_slug(valor_campo, 0)
    k = 1
    print('inicio', slug, len(slug))
    while True:
        registros = model.objects.filter(slug=slug)
        if len(registros) == 0:
            break
        slug = gerar_slug(valor_campo, k)
        print('mudou', slug)
        k += 1
    return slug
