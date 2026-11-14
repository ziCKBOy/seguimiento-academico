# Seguimiento académico

Caso de estudio de *Fundamentos de Algoritmos*: detectar estudiantes en riesgo académico a partir de sus puntajes y entregas, y derivar a seguimiento a quienes cumplen **ambas** condiciones:

- puntaje total **menor a 60**, y
- porcentaje de actividades entregadas **menor a 70 %**.

El análisis completo (diseño, diagrama de flujo y justificación) está en el informe `Actividad_Grupal_sumativa_U3_S3_v2.docx`. Este repositorio contiene el código que lo acompaña.

## Requisitos

Python 3. No usa librerías externas.

## Estructura

| Archivo | Contenido |
|---|---|
| `modelos.py` | Dataclass `Registro(id, entregadas, ptje)`. |
| `propuestaB.py` | Datos (`ids`, `matriz`, `curso`), funciones de apoyo (`obtener_actividades`, `consolidar`) y la **Propuesta B**, el modelo definitivo: un solo recorrido. |
| `algoritmo_base.py` | Algoritmo base (sección 5 del informe): alerta los puntajes < 60 y cuenta el total en riesgo. |
| `propuestaA.py` | Propuesta A (alternativa descartada): tres procesamientos separados, 3n iteraciones. |

## Modelo de datos

- **`ids`**: lista de enteros `[1, ..., 10]`. Cada entero es el identificador de un estudiante.
- **`matriz`**: diccionario `{id: fila}`. Cada fila tiene una celda por actividad, `(puntaje obtenido, entregada)`. El orden de las columnas coincide con el recorrido de las hojas de `curso`.
- **`curso`**: jerarquía `Curso → Módulos → Actividades`. Sus hojas definen las columnas de la matriz y el valor de `total_act`.
- **`Registro`**: resultado consolidado de un estudiante. Su `id` es la clave de su fila en la matriz.

`consolidar(ids, matriz)` recorre los ids, busca cada fila con `matriz[id]` y devuelve la lista de `Registro` con el puntaje total y la cantidad de entregas. Los análisis trabajan solo sobre esa lista.

## Ejecución

Desde la carpeta del proyecto:

```bash
python propuestaB.py
```

```bash
python propuestaA.py
```

```bash
python algoritmo_base.py
```

Salida de `propuestaB.py` con los datos de prueba:

```text
==================================================
 ANÁLISIS DE RENDIMIENTO Y SEGUIMIENTO
==================================================
  [ALERTA]   1 | puntaje:  45 | entregas: 60%
  [DERIVADO] 1 -> seguimiento
  [ALERTA]   2 | puntaje:  55 | entregas: 60%
  [DERIVADO] 2 -> seguimiento
  [ALERTA]   5 | puntaje:  25 | entregas: 40%
  [DERIVADO] 5 -> seguimiento
  [ALERTA]   7 | puntaje:  25 | entregas: 40%
  [DERIVADO] 7 -> seguimiento
  [ALERTA]   9 | puntaje:  15 | entregas: 40%
  [DERIVADO] 9 -> seguimiento

  Total de estudiantes con puntaje < 60: 5
  Total derivados a seguimiento: 5
```

Con estos datos, las propuestas A y B derivan al mismo grupo de estudiantes: 1, 2, 5, 7 y 9.

## Propuestas comparadas

- **Propuesta A**: un recorrido para el puntaje, otro para las entregas y un tercero para cruzar ambos grupos (3n iteraciones, con arreglos de marcas auxiliares).
- **Propuesta B** (seleccionada): un único recorrido que evalúa ambas condiciones sobre cada registro, con un `if` anidado (n iteraciones). Es la que incorpora el nuevo requerimiento al algoritmo base.

En ambos casos el costo de consolidar la matriz es 𝒪(n·m), con `n` estudiantes y `m` actividades, y se paga una sola vez.
