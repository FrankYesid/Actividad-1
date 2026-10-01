# Uso de NotebookLM

NotebookLM es una herramienta externa de consulta y sintesis basada en fuentes que el usuario agrega. En este laboratorio sirve para organizar el material de clase y hacer preguntas sobre documentos; no ejecuta FastAPI, SQL, MongoDB ni celdas Jupyter, y no reemplaza el repositorio ni las pruebas.

## Flujo sugerido

1. Reune fuentes autorizadas: guia de la asignatura, requerimientos, arquitectura, modelo de datos y lecturas proporcionadas por el docente.
2. Crea un cuaderno de NotebookLM para el tema y agrega esas fuentes desde la interfaz del servicio.
3. Pregunta, por ejemplo: “Compara las restricciones del modelo relacional con las referencias del documento MongoDB usando solo estas fuentes”.
4. Comprueba cada respuesta contra la fuente original y conserva citas/referencias al redactar el informe.
5. Lleva ideas y preguntas verificadas al notebook Jupyter para ejecutar consultas con datos sinteticos.

## Cuidado con los datos

- No cargues contrasenas, archivos `.env`, datos personales, datos institucionales reservados ni informacion de produccion.
- Revisa las reglas de privacidad y uso de la institucion antes de cargar documentos.
- Trata respuestas generadas como borradores que deben verificarse; no son resultados de ejecucion ni evidencia experimental.
- El codigo fuente y los notebooks ejecutables permanecen versionados en este proyecto.

## Diferencia entre herramientas

| Herramienta | Uso en el proyecto |
| --- | --- |
| VS Code + Jupyter | Editar y ejecutar celdas Python localmente. |
| PostgreSQL / MongoDB | Persistir y consultar datos del laboratorio. |
| NotebookLM | Consultar y sintetizar fuentes documentales seleccionadas. |