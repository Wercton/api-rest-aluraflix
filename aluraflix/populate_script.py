import os, django
from lorem_text import lorem
from aluraflix.models import Video, Categoria
from random import randint

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

def gerando_video(qtd):
    for i in range(qtd):
        titulo = lorem.words(randint(3,15))
        descricao = lorem.sentence()
        link = 'https://www.youtube.com/watch?v=' + "".join(lorem.words(3).split())
        video = Video(titulo=titulo, descricao=descricao, url=link, categoria=Categoria.objects.get(pk=randint(1,4)))
        video.save()
        
gerando_video(40)
print("Sucesso!")
        
        