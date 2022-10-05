from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from aluraflix.views import VideosViewSet, CategoriasViewSet, ListaVideosCategoria

router = routers.DefaultRouter()
router.register('videos', VideosViewSet, basename='Videos')
router.register('categorias', CategoriasViewSet, basename='Categorias')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('categorias/<int:pk>/videos/', ListaVideosCategoria.as_view())
]