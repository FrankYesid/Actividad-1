# Requerimientos del laboratorio

## Objetivo

Construir y estudiar un monolito modular que permita comparar el modelado y la consulta de datos estructurados en SQL con el almacenamiento de documentos flexibles en MongoDB, dentro de un contexto academico de mineria de datos.

## Alcance

- Una API FastAPI desplegada como una sola aplicacion.
- PostgreSQL para cursos y estudiantes, con claves, restricciones e indices.
- MongoDB para observaciones y anotaciones con etiquetas y campos opcionales.
- Dos notebooks Jupyter para experimentar con SQL y documentos.
- Datos sinteticos; no se incluyen datos personales reales ni credenciales de servicios.

Fuera del alcance: microservicios, autenticacion, interfaz web, despliegue cloud y procesos de entrenamiento de modelos.

## Requerimientos funcionales

| ID | Requerimiento | Criterio de aceptacion |
| --- | --- | --- |
| RF-01 | Consultar el estado de la API | `GET /health` responde HTTP 200 y `status=ok`. |
| RF-02 | Crear y listar cursos | `POST /api/courses` persiste nombre y area en PostgreSQL; `GET /api/courses` los devuelve. |
| RF-03 | Crear y listar estudiantes | El alta valida que exista el curso y conserva la relacion por clave foranea. |
| RF-04 | Evitar duplicados relacionales | Nombre de curso y correo de estudiante son unicos; un duplicado devuelve HTTP 409. |
| RF-05 | Crear y listar observaciones | MongoDB conserva titulo, contenido, etiquetas, curso opcional y fecha de creacion. |
| RF-06 | Explorar conceptos | Los notebooks muestran ejemplos reproducibles sin depender de datos privados. |
| RF-07 | Configurar conexiones | Las URI y el nombre de la base se leen de variables de entorno con valores locales de desarrollo. |

## Requerimientos no funcionales

- **RNF-01 Mantenibilidad:** separar API, configuracion, persistencia, modelos y esquemas sin dividir el despliegue.
- **RNF-02 Validacion:** validar entradas con Pydantic y declarar restricciones de integridad en SQL.
- **RNF-03 Portabilidad:** poder iniciar PostgreSQL y MongoDB con Docker Compose en un equipo local.
- **RNF-04 Seguridad de aula:** no versionar `.env`; usar solamente credenciales desechables locales.
- **RNF-05 Comprensibilidad:** documentar decisiones y entregar ejemplos pequenos en espanol.

## Casos de uso

1. **Registrar curso y estudiante:** crear curso, copiar su `id`, crear estudiante con ese `course_id` y consultar el listado.
2. **Registrar observacion exploratoria:** guardar una nota con etiquetas libres en MongoDB y recuperarla desde el endpoint de observaciones.
3. **Comparar persistencias:** expresar relaciones y restricciones con tablas SQL; representar notas de forma documental cuando sus atributos varian.
4. **Preparar una consulta analitica:** extraer datos de cada origen y decidir como validarlos, limpiarlos y relacionarlos antes de analizarlos en un notebook.

## Restricciones y supuestos

- La API necesita ambos motores activos para usar sus operaciones correspondientes; el endpoint de salud solo verifica que el proceso web responde.
- El script SQL de inicializacion de Compose se ejecuta solo cuando el volumen de PostgreSQL se crea por primera vez.
- MongoDB se deja sin autenticacion dentro del entorno local de aula. No se debe exponer ese puerto en una red publica.