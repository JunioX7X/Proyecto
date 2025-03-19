# Proyecto API con FastAPI y Docker

Este repositorio contiene una implementación de una API REST desarrollada con FastAPI y containerizada con Docker, siguiendo prácticas de versionamiento Git.

## Estructura del Proyecto

```
mi-fastapi-proyecto/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── routers/
│       ├── __init__.py
│       └── items.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── README.md
```

## Características

- API REST completa con operaciones CRUD
- Documentación automática con Swagger UI (accesible en `/docs`)
- Containerización con Docker
- Flujo de trabajo Git con ramas main, staging, develop y features

## Instrucciones de Ejecución

### Ejecución Local

1. Clonar el repositorio
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar servidor: `uvicorn app.main:app --reload`
4. Acceder a la API: [http://localhost:8000](http://localhost:8000)
5. Documentación: [http://localhost:8000/docs](http://localhost:8000/docs)

### Ejecución con Docker

```bash
# Construir imagen
docker build -t miapifastapi:latest .

# Ejecutar contenedor
docker run -p 8000:8000 miapifastapi:latest
```

## Docker Hub

La imagen está disponible en Docker Hub:

```bash
docker pull tuusuario/miapifastapi:latest
```

## Estrategia de Versionamiento Git

Este proyecto implementa GitFlow con las siguientes ramas:
- `main`: Código en producción
- `staging`: Código listo para pruebas pre-producción
- `develop`: Rama de integración para desarrollo
- `feature/*`: Ramas para desarrollo de características específicas

## Endpoints Disponibles

- `GET /`: Información general de la API
- `GET /items`: Listar todos los items
- `POST /items`: Crear un nuevo item
- `GET /items/{item_id}`: Obtener un item específico
