# Memoria

## Getting Started

### Requisito previo

Para el desarrollo local de la app necesitas tener Docker instalado en tu PC (Docker Desktop con Docker Compose).

### Levantar el entorno local

Desde la raiz del proyecto ejecuta:

```bash
docker compose up --build
```

Este comando construye las imagenes, levanta los contenedores y monta los volumenes para desarrollo.

### Base de datos local

Las credenciales de PostgreSQL para desarrollo local estan definidas como valores por defecto en el backend, en `backend/dcc_catalog/settings.py`:

- `POSTGRES_DB=dcc_catalog`
- `POSTGRES_USER=postgres`
- `POSTGRES_PASSWORD=password`
- `POSTGRES_HOST=localhost`
- `POSTGRES_PORT=5432`

Si te quieres conectar con tu cliente favorito (por ejemplo, DBeaver) desde tu PC, puedes usar esos mismos datos.

Nota: dentro de Docker, el backend usa `POSTGRES_HOST=db` segun `docker-compose.yml`.

### Manejo de dependencias

- Backend: manejo de dependencias con Poetry (`pyproject.toml`).
- Frontend: manejo de dependencias con npm en React (`frontend/package.json`).

