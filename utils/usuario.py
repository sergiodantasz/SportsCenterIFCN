def formatar_url_foto(url: str) -> str:
    nova_url_foto = ''
    for i, c in enumerate(url):
        if 'alunos' in url:
            if 20 >= i >= 14:
                continue
        else:
            if 19 >= i >= 13:
                continue
        nova_url_foto += c
    return nova_url_foto
