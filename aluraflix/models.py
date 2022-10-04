from django.db import models


class Video(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    url = models.CharField(max_length=50)