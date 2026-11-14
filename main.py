from modelos import Registro

###################################################################################
#DEFINICIONES
# Arreglo lineal: cada índice i identifica al estudiante de la fila i de la matriz.
ids = ["A01", "A02", "A03", "A04"]

# Matriz bidimensional: filas = estudiantes (mismo orden que ids),
# columnas = actividades (mismo orden que obtener_actividades(curso)).
# Cada celda: (puntaje obtenido, True si fue entregada / False si no).
matriz = [
    [(10, True),  (15, True),  (20, True),  (0, False),  (0, False)],  # A01
    [(20, True),  (25, True),  (10, True),  (0, False),  (0, False)],  # A02
    [(30, True),  (30, True),  (20, True),  (0, False),  (0, False)],  # A03
    [(20, True),  (20, True),  (20, True),  (20, True),  (10, True)],  # A04
]

# Jerarquía simple (árbol): Curso -> Módulos -> Actividades (hojas).
curso = {
    "Fundamentos de Algoritmos": {
        "Módulo 1": ["Act 1", "Act 2"],
        "Módulo 2": ["Act 3", "Act 4", "Act 5"],
    }
}

###################################################################################


def obtener_actividades(arbol):
    """Recorre la jerarquía del curso y retorna la lista de actividades (hojas)."""
    lista_act = []
    for modulos in arbol.values():
        for acts in modulos.values():
            lista_act.extend(acts)
    return lista_act


def consolidar(lista_ids, tabla):
    """Convierte la matriz en una lista de Registro con puntaje total y entregas por estudiante."""
    lista_est = []
    for i in range(len(tabla)):
        puntaje = 0
        entregadas = 0
        for j in range(len(tabla[i])):
            pts, entregada = tabla[i][j]
            puntaje += pts
            if entregada:
                entregadas += 1
        lista_est.append(Registro(lista_ids[i], entregadas, puntaje))
    return lista_est


# 5. Procesamiento de información (Algoritmo base)
def analizar_rendimiento(estudiantes, id_busc):
    """Busca un ID e imprime alertas y el total de estudiantes con puntaje < 60."""
    cant_riesgo = 0

    for est in estudiantes:
        if est.id == id_busc:
            print("Registro encontrado: ", est.id)

        if est.ptje < 60:
            cant_riesgo = cant_riesgo + 1
            print("Alerta de rendimiento. ID: ", est.id)

    print("Estudiantes con puntaje < 60: ", cant_riesgo)


# 6. Resolución de nuevos requerimientos
def detectar_seguimiento(estudiantes, total_act):
    """Retorna los IDs con puntaje < 60 y entregas < 70 % para derivar a seguimiento."""
    lista_seg = []

    for est in estudiantes:
        pct_ent = (est.entregadas / total_act) * 100

        if (est.ptje < 60) and (pct_ent < 70.0):
            lista_seg.append(est.id)
            print("Estudiante derivado: ", est.id)

    return lista_seg


if __name__ == "__main__":
    actividades = obtener_actividades(curso)
    total_act = len(actividades)
    estudiantes = consolidar(ids, matriz)

    analizar_rendimiento(estudiantes, "A02")
    lista_seg = detectar_seguimiento(estudiantes, total_act)
