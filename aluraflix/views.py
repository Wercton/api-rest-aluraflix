from rest_framework import viewsets
from aluraflix.models import Video
from aluraflix.serializer import VideoSerializer


class VideosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os vídeos"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer