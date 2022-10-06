from django.db import models


class Categoria(models.Model):
    titulo = models.CharField(max_length=20)
    cor = models.CharField(max_length=7)
    
    def __str__(self):
         return self.titulo


class Video(models.Model):
    titulo = models.CharField(max_length=75)
    descricao = models.TextField()
    url = models.URLField(max_length=200)
    categoria = models.ForeignKey(Categoria, default=1, on_delete=models.CASCADE)
    
    def __str__(self):
         return self.titulo