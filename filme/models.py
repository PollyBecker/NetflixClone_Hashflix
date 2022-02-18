from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.
#criar filmes

LISTA_CATEGORIAS=(
    ('DESENHOS', 'Desenhos'),
    ('FAMILIA', 'Família'),
    ('SERIES', 'Séries'),
)


class Filme(models.Model):
    tilulo=models.CharField(max_length=100)
    visualizados =models.IntegerField(default=0)
    lancamento=models.DateTimeField(default=timezone.now)
    thumb=models.ImageField(upload_to='thumb_filmes')
    descricao=models.TextField(max_length=1000)
    categoria=models.CharField(max_length=20,choices=LISTA_CATEGORIAS)

    def __str__(self):
        return self.tilulo

class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.titulo

class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField('Filme')


