from rest_framework import serializers
from aluraflix.models import Video, Categoria
from aluraflix.validators import hex_valido


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
    
    def validate(self, data):
        if not hex_valido(data['cor']):
            raise serializers.ValidationError("Código hexadecimal inválido.")
        return data


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        
class ListaVideosCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['titulo', 'descricao', 'url']