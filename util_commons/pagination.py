from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination):
    """
    Clase de paginación personalizada para las API.

    Esta clase hereda de `PageNumberPagination` del framework Django REST
    Framework y permite personalizar la paginación de los resultados en
    las vistas de la API.
    """

    # Número de elementos por página
    page_size = 10
    # Parámetro para especificar el tamaño de página
    page_size_query_param = "page_size"
    # Tamaño máximo de página permitido
    max_page_size = 100
    # Parámetro para especificar el número de página
    page_query_param = "page"
