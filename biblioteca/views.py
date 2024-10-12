from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import Libro, Autor
from .serializers import LibroSerializer, AutorSerializer
from .services import eliminar_autor
from util_commons.pagination import CustomPagination


class LibroViewSet(ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    pagination_class = CustomPagination


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    pagination_class = CustomPagination

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        eliminar_autor(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
