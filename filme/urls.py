from django.urls import path , include, reverse_lazy
from .views import Homepage,Homefilmes , DetalhesFilmes, PesquisaFilmes, PaginaPerfil, CriarConta
from django.contrib.auth import views as auth_views

app_name= 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(),name='homefilmes'),
    path("filmes/<int:pk>", DetalhesFilmes.as_view(),name='detalhesfilmes'),
    path("pesquisa/", PesquisaFilmes.as_view(),name='pesquisa'),
    path("login/", auth_views.LoginView.as_view(template_name='login.html') ,name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='logout.html') ,name='logout'),
    path("editarperfil/<int:pk>", PaginaPerfil.as_view(), name='editar'),
    path("criarconta/", CriarConta.as_view(), name='criarconta'),
    path("mudarsenha/", auth_views.PasswordChangeView.as_view(template_name='editar.html', success_url=reverse_lazy('filmes:homefilmes')) ,name='mudarsenha'),
]
