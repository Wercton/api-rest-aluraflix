from django.db import models


class Video(models.Model):
    titulo = models.CharField(max_length=75)
    descricao = models.TextField()
    url = models.URLField(max_length=200)