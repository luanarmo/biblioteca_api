from django.db import models


class Autor(models.Model):
    """
    Modelo que representa a un autor de libros.

    Atributos:
        nombre (CharField): El nombre del autor. Debe tener un máximo de 50 caracteres.
        apellido (CharField): El apellido del autor. Debe tener un máximo de 50 caracteres.
        fecha_nacimiento (DateField): La fecha de nacimiento del autor.
    """

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self) -> str:
        """
        Método que devuelve el nombre completo del autor.
        """
        return f"{self.nombre} {self.apellido}"


class Libro(models.Model):
    """
    Modelo que representa un libro.

    Atributos:
        titulo (CharField): El título del libro. Debe tener un máximo de 100 caracteres.
        fecha_publicacion (DateField): La fecha en la que se publicó el libro.
        autor_id (ForeignKey): Relación con el modelo Autor. Representa el autor del libro.
    """

    titulo = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        """
        Método que devuelve el título del libro.
        """
        return self.titulo
