from os.path import splitext


def caminho_capa_noticia(instance, filename):
    arquivo, extensao = splitext(filename)
    arquivo_renomeado = instance.slug + extensao
    return f'noticias/capas/{arquivo_renomeado}'
