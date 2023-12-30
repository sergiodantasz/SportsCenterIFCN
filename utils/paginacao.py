from math import ceil

from django.core.paginator import Paginator


def criar_range_paginacao(range_paginas: list, qtd_paginas: int, pagina_atual: int):
    meio_range = ceil(qtd_paginas / 2)
    inicio_range = pagina_atual - meio_range
    final_range = pagina_atual + meio_range
    total_paginas = len(range_paginas)
    if inicio_range < 0:
        offset_inicio_range = abs(inicio_range)
        inicio_range = 0
        final_range += offset_inicio_range
    if final_range > total_paginas:
        inicio_range -= abs(total_paginas - final_range)
    paginacao = range_paginas[inicio_range:final_range]
    return {
        'paginacao': paginacao,
        'range_paginas': range_paginas,
        'qtd_paginas': qtd_paginas,
        'pagina_atual': pagina_atual,
        'total_paginas': total_paginas,
        'inicio_range': inicio_range,
        'final_range': final_range,
        'primeira_pagina_fora_do_range': pagina_atual > meio_range,
        'ultima_pagina_fora_do_range': final_range < total_paginas
    }


def criar_paginacao(request, queryset, per_page):
    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1
    paginator = Paginator(queryset, per_page)
    page_obj = paginator.get_page(current_page)
    pagination_range = criar_range_paginacao(
        range_paginas=paginator.page_range,
        qtd_paginas=5,
        pagina_atual=current_page
    )
    return page_obj, pagination_range
