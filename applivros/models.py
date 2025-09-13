from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    idade = models.IntegerField()
    email = models.EmailField()

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return f"{self.titulo}-{self.autor}"
    
class LivroFavorito(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE) 

    class Meta:
        unique_together = ('pessoa', 'livro') 