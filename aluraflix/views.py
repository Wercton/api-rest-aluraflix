from rest_framework import viewsets, generics, filters
from aluraflix.models import Video, Categoria
from aluraflix.serializers import VideoSerializer, CategoriaSerializer, ListaVideosCategoriaSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class CategoriasViewSet(viewsets.ModelViewSet):
    """Exibindo todos as categorias"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id', 'titulo']
    search_fields = ['titulo']

class VideosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os vídeos"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id', 'titulo']
    search_fields = ['titulo', 'descricao']
    
class ListaVideosCategoria(generics.ListAPIView):
    """Listando os vídeos de uma categoria"""
    def get_queryset(self):
        queryset = Video.objects.filter(categoria=self.kwargs['pk'])
        return queryset
    serializer_class = ListaVideosCategoriaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id', 'titulo']
    search_fields = ['titulo', 'descricao']