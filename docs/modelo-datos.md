# Modelo de datos

## Relacional: PostgreSQL

| Tabla | Columnas principales | Regla |
| --- | --- | --- |
| `courses` | `id`, `name`, `area` | `name` es unico; `area` puede indexarse para filtros. |
| `students` | `id`, `name`, `email`, `course_id` | `email` es unico y `course_id` referencia `courses.id`. |

La relacion es uno a muchos: un curso puede tener varios estudiantes; cada estudiante pertenece a un curso. Las restricciones protegen la integridad incluso si otra aplicacion escribe en la base.

## Documental: MongoDB

Ejemplo conceptual de documento en `observations`:

```json
{
  "title": "Sesion 1",
  "content": "Se revisaron valores faltantes en la muestra",
  "tags": ["calidad", "exploracion"],
  "course_id": 1,
  "created_at": "2026-09-30T10:00:00Z"
}
```

MongoDB agrega `_id`. `course_id` permite asociar la observacion con un curso por convencion de la aplicacion, pero no es una clave foranea validada por el motor.

## Criterio para elegir

- Elige SQL cuando la estructura es conocida, hay relaciones y necesitas restricciones, joins o transacciones locales.
- Elige documentos cuando la unidad de lectura es un agregado y los atributos varian entre registros, como notas de exploracion con metadatos opcionales.
- No elijas una base solo por su etiqueta “estructurado/no estructurado”: evalua consultas, consistencia, evolucion de esquema, volumen y operacion.
- Texto libre en un documento sigue teniendo estructura externa (campos, tipos, indices); “no estructurado” no significa “sin modelo”.

## Preguntas para el ejercicio

1. ¿Que inconsistencia podria producirse si se borra un curso aun cuando una observacion conserva su `course_id`?
2. ¿Que restricciones de estudiante seria dificil mantener solo en MongoDB?
3. ¿Cuando convendria normalizar las etiquetas y cuando convendria conservarlas como arreglo?
4. ¿Que campos se deberian limpiar o anonimizar antes de usar los datos para mineria?