from rest_framework import viewsets, generics
from aluraflix.models import Video, Categoria
from aluraflix.serializer import VideoSerializer, CategoriaSerializer, ListaVideosCategoriaSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class CategoriasViewSet(viewsets.ModelViewSet):
    """Exibindo todos as categorias"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class VideosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os vídeos"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ListaVideosCategoria(generics.ListAPIView):
    """Listando os vídeos de uma categoria"""
    def get_queryset(self):
        queryset = Video.objects.filter(categoria=self.kwargs['pk'])
        return queryset
    serializer_class = ListaVideosCategoriaSerializer