from rest_framework import serializers
from .models import Libro, Autor


class AutorSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Autor
    """

    class Meta:
        model = Autor  # Especifica el modelo asociado con el serializador
        exclude = ["id"]  # Excluye el campo 'id' pero incluye todos los demás


class LibroSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Libro
    """

    class Meta:
        model = Libro  # Especifica el modelo asociado con el serializador
        exclude = ["id"]  # Excluye el campo 'id' pero incluye todos los demás
