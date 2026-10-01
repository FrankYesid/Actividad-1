# Guia de uso

## Preparacion

Desde PowerShell, en la carpeta del proyecto:

```powershell
Copy-Item .env.example .env
docker compose up -d
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Si la politica de ejecucion impide activar el entorno, habilita scripts solo para la sesion con `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` y vuelve a activarlo.

## Probar la API

Visita `/docs` en el servidor local para ver contratos y enviar peticiones. Orden sugerido:

1. `POST /api/courses` con `{"name":"Mineria de datos","area":"Analitica"}`.
2. Usa el `id` de la respuesta para crear un estudiante con `POST /api/students`.
3. Crea una observacion con `POST /api/observations`; `course_id` es opcional.
4. Usa los endpoints `GET` correspondientes para revisar cada almacenamiento.

Los conflictos de unicidad responden `409`; un curso inexistente al crear estudiante responde `404`; si MongoDB no esta disponible, las rutas de observaciones responden `503`.

## Notebooks

Abre los archivos de `notebooks/` en VS Code, selecciona un kernel Python del entorno `.venv` y ejecuta las celdas en orden. Los ejemplos principales usan bibliotecas estandar para que se puedan ejecutar sin levantar bases de datos. Las llamadas de API descritas aqui requieren Compose y Uvicorn activos.

## Detener servicios

```powershell
docker compose down
```

Esto conserva los volumenes locales. Para el laboratorio, elimina datos solo cuando sea intencional mediante `docker compose down -v`; esa opcion borra los datos guardados en los volumenes.

## Solucion de problemas

- **Puerto ocupado:** cambia el puerto publicado en `docker-compose.yml` y ajusta las URI en `.env`.
- **La tabla no existe:** confirma que el contenedor PostgreSQL se inicializo y revisa si el volumen ya existia antes de agregar `schema.sql`.
- **Mongo 503:** confirma `docker compose ps` y que `MONGO_URL` apunte al puerto local correcto.
- **Modulo no encontrado:** activa `.venv` e instala `requirements.txt` desde la raiz del proyecto.