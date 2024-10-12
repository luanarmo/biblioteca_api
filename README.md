# Nombre del Proyecto

Esta API RESTful está diseñada para la gestión de una biblioteca, facilitando la creación, lectura, actualización y eliminación (CRUD) de información relacionada con libros y autores. Proporciona una interfaz sencilla y eficiente para interactuar con los datos, permitiendo a los usuarios gestionar fácilmente su colección de libros y la información de los autores asociados.

## Tabla de Contenidos

- [Clonar el repositorio](#clonar-el-repositorio)
- [Configurar el entorno de desarrollo](#configurar-el-entorno-de-desarrollo)
- [Ejecutar la aplicación](#ejecutar-la-aplicación)
- [Realizar peticiones a la API](#realizar-peticiones-a-la-api)

## Clonar el repositorio

Para clonar este repositorio, utiliza el siguiente comando:

```
git clone git@github.com:luanarmo/biblioteca_api.git
```

## Configurar el entorno de desarrollo

1. Navega al directorio del proyecto:

   ```
   cd biblioteca_api
   ```

2. Crea un entorno virtual:

   ```
   python -m venv venv
   ```

3. Activa el entorno virtual:

   - En Windows:

     ```
     venv\Scripts\activate
     ```

   - En macOS/Linux:

     ```
     source venv/bin/activate
     ```

4. Instala las dependencias:

   ```
   pip install -r requirements.txt
   ```

5. Crea un archivo `.env` en la raíz del proyecto y configura las variables de entorno necesarias:

   ```
   DATABASE_NAME=nombre_de_la_base_de_datos
   DATABASE_USER=usuario_de_la_bd
   DATABASE_PASSWORD=contraseña_de_la_bd
   DATABASE_HOST=host
   DATABASE_PORT=puerto
   ```

## Ejecutar la aplicación

Antes de ejecutar la aplicación, es necesario aplicar las migraciones en la base de datos con el siguiente comando:

```
python manage.py migrate
```

Para ejecutar la aplicación, utiliza el siguiente comando:

```
python manage.py runserver
```

La aplicación estará disponible en `http://127.0.0.1:8000/`.

## Realizar peticiones a la API

A continuación, se presentan ejemplos de cómo realizar peticiones a la API utilizando herramientas como Postma (en este caso Insomnia).

### Obtener todos los autores

![image](https://github.com/user-attachments/assets/19187a2f-7d36-4981-ac81-160dc3a135dd)


### Crear un nuevo autor

![image](https://github.com/user-attachments/assets/2b159042-8ae7-4e87-8313-e60a15cc0b66)

### Actualizar autor

![image](https://github.com/user-attachments/assets/e42bbf25-2411-4372-aefc-71c06771100f)

### Obtener autor

![image](https://github.com/user-attachments/assets/31e6bce8-0150-4bcf-89ca-4c1d253d1210)

### Eliminar autor

![image](https://github.com/user-attachments/assets/95095f27-71a1-44b4-9bf1-0e171844f484)

### Intentar eliminar autor con libros relacionados

![image](https://github.com/user-attachments/assets/3071f424-ef2f-4d84-9102-62900b36ad61)


### Obtener todos los libros

![image](https://github.com/user-attachments/assets/af9ccc25-cf7a-42f4-99ec-95b1820d5f4b)


### Crear un nuevo libro

![image](https://github.com/user-attachments/assets/f0c58586-956e-41a5-afec-9129a2cb8b11)


### Actualizar libro

![image](https://github.com/user-attachments/assets/9e0a503b-c6b3-4745-893d-ae5cb2b2bf33)


### Obtener libro

![image](https://github.com/user-attachments/assets/746f151c-d4c1-498c-a311-0c07c1acddc6)


### Eliminar libro

![image](https://github.com/user-attachments/assets/453e4907-9650-47dd-9e23-bd30faea2d71)



