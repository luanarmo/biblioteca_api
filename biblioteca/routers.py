from rest_framework.routers import DefaultRouter
from . import views

# Crear una instancia del enrutador por defecto
router = DefaultRouter()

# Registrar el ViewSet para el modelo Libro
router.register(
    prefix="libros",  # Prefijo de la URL para acceder a los libros
    viewset=views.LibroViewSet,  # ViewSet que manejará las solicitudes
    basename="libros",  # Nombre base para las URL generadas
)

# Registrar el ViewSet para el modelo Autor
router.register(
    prefix="autores",  # Prefijo de la URL para acceder a los autores
    viewset=views.AutorViewSet,  # ViewSet que manejará las solicitudes
    basename="autores",  # Nombre base para las URL generadas
)
