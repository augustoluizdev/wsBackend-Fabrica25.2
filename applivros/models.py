from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    idade = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    capa_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.autor})"

class LivroFavorito(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('pessoa', 'livro')