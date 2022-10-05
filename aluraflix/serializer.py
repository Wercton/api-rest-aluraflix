from rest_framework import serializers
from aluraflix.models import Video, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        
class ListaVideosCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['titulo', 'descricao', 'url']