from django.contrib import admin
from aluraflix.models import Video, Categoria

class Videos(admin.ModelAdmin):
    list_display = ('id', 'titulo','descricao', 'url', 'categoria')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 20
    
class Categorias(admin.ModelAdmin):
    list_display = ('id', 'titulo','cor')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 20
    
admin.site.register(Video, Videos)
admin.site.register(Categoria, Categorias)