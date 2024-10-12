from django.urls import path, include
from .routers import router

# Nombre de la aplicación para el espacio de nombres de las URL
app_name = "biblioteca_app"

# Definición de las URL para la aplicación
urlpatterns = [
    path("", include(router.urls)),  # Incluye las rutas del enrutador
]
