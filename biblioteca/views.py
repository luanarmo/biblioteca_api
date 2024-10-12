from rest_framework.viewsets import ModelViewSet

from .models import Libro, Autor
from .serializers import LibroSerializer, AutorSerializer
from util_commons.pagination import CustomPagination


class LibroViewSet(ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    pagination_class = CustomPagination


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    pagination_class = CustomPagination
