from rest_framework.exceptions import ValidationError
from .models import Autor, Libro


def eliminar_autor(autor: Autor) -> None:
    """
    Elimina un autor de la base de datos si no tiene libros asociados.

    Este método verifica si el autor tiene libros asociados. Si es así,
    se lanza una excepción `ValidationError` para informar que no se puede
    eliminar el autor. Si no hay libros asociados, el autor se elimina.

    Args:
        autor (Autor): La instancia del autor que se desea eliminar.

    Raises:
        ValidationError: Si el autor tiene libros asociados.
    """

    # Verifica si existen libros asociados al autor
    if Libro.objects.filter(autor=autor).exists():
        raise ValidationError(
            {"autor": "No se puede eliminar el autor porque tiene libros asociados"}
        )

    # Elimina el autor si no tiene libros asociados
    autor.delete()
