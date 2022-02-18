from .models import Filme


def lista_filmes_recentes(request):
    lista_filmes =Filme.objects.all().order_by('-lancamento')[0:8]
    if lista_filmes:
        filme_destaque = lista_filmes[0]
    else:
        filme_destaque=None
    return {'lista_filmes_recentes':lista_filmes, 'filme_destaque': filme_destaque}

def lista_filmes_alta(request):
    lista_filmes =Filme.objects.all().order_by('-visualizados')[0:8]
    return {'lista_filmes_alta': lista_filmes }

