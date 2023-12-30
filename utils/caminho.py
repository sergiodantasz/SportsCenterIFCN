from os.path import splitext


def gerar_caminho_anexo_arquivo(instancia, arquivo):
    return f'anexos/arquivos/{instancia.arquivo.slug}/{arquivo}'


def gerar_caminho_capa(instancia, arquivo):
    model = instancia.__class__.__name__
    slug = instancia.slug
    _, extensao = splitext(arquivo)
    caminho_capa = f'capas/{model.lower()}s/{slug + extensao}'
    return caminho_capa
