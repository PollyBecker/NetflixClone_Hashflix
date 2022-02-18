from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from .forms import CriarContaForm, FormHome
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# fbv function based views
# def homepage(request):
#     return render(request, 'homepage.html')
#cbv class based views

class Homepage(FormView):
    template_name = 'homepage.html'
    form_class = FormHome


    def get(self, request, *args, **kwargs ):
        #mandar o user pra pafina de filme se ele estiver logado
        if request.user.is_authenticated:
            return redirect( 'filme:homefilmes' )
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        email = self.request.POST.get('email')
        usuario = Usuario.objects.filter(email=email)
        if usuario:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')

# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render( request, 'homefilmes.html', context )

class Homefilmes( LoginRequiredMixin, ListView):
    template_name = 'homefilmes.html'
    model = Filme
    #list_view me retorna uma lista com nome object_list

class DetalhesFilmes(LoginRequiredMixin, DetailView):
    template_name = 'detalhesfilmes.html'
    model = Filme
    #detailview me retorna a variavel object

    def get(self, request, *args, **kwargs ):
        #contabilizando as views
        filme = self.get_object()
        filme.visualizados +=1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super( DetalhesFilmes, self).get_context_data(**kwargs)
        lista_filmes =Filme.objects.filter(categoria=self.get_object().categoria)[0:3]
        context["lista_filmes_relacionados"] = lista_filmes

        return context

class PesquisaFilmes(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Filme

    def get_queryset(self):
        pesquisado=self.request.GET.get('query')
        if pesquisado:
            object_list=Filme.objects.filter(tilulo__icontains=pesquisado)
            return object_list
        else:
            return None


class PaginaPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editar.html'
    model = Usuario
    fields = ['first_name','last_name','email']

    def get_success_url(self):
        return reverse('filme:homefilmes')


class CriarConta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')

