# Monolito Datos Lab

Proyecto de aula para estudiar una aplicacion monolitica modular que combina PostgreSQL (datos estructurados) y MongoDB (documentos flexibles) en una API FastAPI.

## Inicio rapido en Windows

1. Instala Docker Desktop y Python 3.12 o superior.
2. Crea el archivo local de configuracion:

   ```powershell
   Copy-Item .env.example .env
   ```

3. Inicia las bases de datos:

   ```powershell
   docker compose up -d
   ```

4. Crea y activa un entorno Python, e instala las dependencias:

   ```powershell
   py -3.12 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   ```

5. Inicia la API:

   ```powershell
   python -m uvicorn app.main:app --reload
   ```

Abre `http://127.0.0.1:8000/docs` para probar la API interactiva. La comprobacion de estado esta en `http://127.0.0.1:8000/health`.

## Recorrido sugerido

1. Lee [los requerimientos](docs/requerimientos.md) y [la arquitectura](docs/arquitectura.md).
2. Ejecuta las celdas de `notebooks/01_sql_estructurado.ipynb` y `notebooks/02_documentos_mongodb.ipynb`.
3. Crea cursos y estudiantes en PostgreSQL; crea observaciones con etiquetas en MongoDB.
4. Compara los dos modelos con las preguntas de [modelo de datos](docs/modelo-datos.md).
5. Usa la [guia de NotebookLM](docs/notebooklm.md) para organizar y consultar fuentes, sin confundirlo con el entorno de ejecucion.

## API de ejemplo

```powershell
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/api/courses `
  -ContentType 'application/json' -Body '{"name":"Mineria de datos","area":"Analitica"}'

Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/api/students `
  -ContentType 'application/json' -Body '{"name":"Ana Ruiz","email":"ana@example.edu","course_id":1}'

Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/api/observations `
  -ContentType 'application/json' -Body '{"title":"Sesion 1","content":"Se revisaron valores faltantes","tags":["calidad","exploracion"],"course_id":1}'
```

Listados disponibles: `GET /api/courses`, `GET /api/students` y `GET /api/observations`.

## Pruebas

Con el entorno virtual activo:

```powershell
python -m pytest
```

## Estructura

- `app/`: aplicacion monolitica organizada por responsabilidades.
- `scripts/schema.sql`: tablas, restricciones, indices y curso semilla de PostgreSQL.
- `notebooks/`: practicas ejecutables y autocontenidas para conceptos SQL/documentos.
- `docs/`: requerimientos, arquitectura, uso, modelo de datos, glosario y NotebookLM.
- `docker-compose.yml`: servicios locales de PostgreSQL y MongoDB; la API se ejecuta desde el entorno Python.

Los datos de Compose son credenciales locales unicamente para el laboratorio. No las reutilices en un entorno real.