from re import search
from rest_framework import serializers
from aluraflix.models import Video, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
    def validate_cor(self, cor):
        if not search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', cor):
            raise serializers.ValidationError("Código hexadecimal inválido.")
        else:
            return cor

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        
class ListaVideosCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['titulo', 'descricao', 'url']