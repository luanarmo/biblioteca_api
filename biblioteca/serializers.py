from rest_framework import serializers
from .models import Libro, Autor


class AutorSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Autor
    """

    def validate_nombre(self, value):
        """
        Valida el campo 'nombre' del autor para que tenga al menos 3 caracteres y no sea solo números
        """
        if len(value) < 3:
            raise serializers.ValidationError(
                "El nombre del autor debe tener al menos 3 caracteres"
            )

        if value.isdigit():
            raise serializers.ValidationError(
                "El título del libro no puede ser solo números"
            )

        return value

    def validate_apellido(self, value):
        """
        Valida el campo 'apellido' del autor para que tenga al menos 3 caracteres y no sea solo números
        """

        if len(value) < 3:
            raise serializers.ValidationError(
                "El apellido del autor debe tener al menos 3 caracteres"
            )

        if value.isdigit():
            raise serializers.ValidationError(
                "El título del libro no puede ser solo números"
            )

        return value

    class Meta:
        model = Autor  # Especifica el modelo asociado con el serializador
        exclude = ["id"]  # Excluye el campo 'id' pero incluye todos los demás


class LibroSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Libro
    """

    def validate_titulo(self, value):
        """
        Valida el campo 'titulo' del libro para que tenga al menos 3 caracteres y no sea solo números
        """
        if len(value) < 3:
            raise serializers.ValidationError(
                "El título del libro debe tener al menos 3 caracteres"
            )

        if value.isdigit():
            raise serializers.ValidationError(
                "El título del libro no puede ser solo números"
            )

        return value

    class Meta:
        model = Libro  # Especifica el modelo asociado con el serializador
        exclude = ["id"]  # Excluye el campo 'id' pero incluye todos los demás
