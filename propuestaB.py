from modelos import Registro

###################################################################################
#DEFINICIONES
# Arreglo lineal: cada índice i identifica al estudiante de la fila i de la matriz.
ids = ["A01", "A02", "A03", "A04", "A05", "A06", "A07", "A08", "A09", "A10"]

# Matriz bidimensional: filas = estudiantes (mismo orden que ids),
# columnas = actividades (mismo orden que obtener_actividades(curso)).
# Cada celda: (puntaje obtenido, True si fue entregada / False si no).
matriz = [
    [(10, True),  (15, True),  (20, True),  (0, False),  (0, False)],  # A01
    [(20, True),  (25, True),  (10, True),  (0, False),  (0, False)],  # A02
    [(30, True),  (30, True),  (20, True),  (0, False),  (0, False)],  # A03
    [(20, True),  (20, True),  (20, True),  (20, True),  (10, True)],  # A04
    [(15, True),  (10, True),  (0, False),  (0, False),  (0, False)],  # A05 - 2 entregas
    [(25, True),  (30, True),  (25, True),  (20, True),  (15, True)],  # A06
    [(10, True),  (0, False),  (15, True),  (0, False),  (0, False)],  # A07
    [(30, True),  (25, True),  (30, True),  (25, True),  (0, False)],  # A08
    [(5,  True),  (10, True),  (0, False),  (0, False),  (0, False)],  # A09
    [(20, True),  (20, True),  (20, True),  (15, True),  (10, True)],  # A10
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


# Propuesta B (modelo definitivo): un solo recorrido de todos los estudiantes que cuenta
# y muestra a los de puntaje < 60 y deriva a seguimiento a los que además tienen
# entregas < 70 %.
def analizar_estudiantes(estudiantes, total_act):
    """Recorre todos los estudiantes una sola vez: alerta puntaje < 60 y deriva si entregas < 70 %."""
    cant_riesgo = 0
    lista_seg = []

    for est in estudiantes:
        pct_ent = (est.entregadas / total_act) * 100

        if est.ptje < 60:
            cant_riesgo = cant_riesgo + 1
            print(f"  [ALERTA]   {est.id} | puntaje: {est.ptje:>3} | entregas: {pct_ent:.0f}%")

            if pct_ent < 70.0:
                lista_seg.append(est.id)
                print(f"  [DERIVADO] {est.id} -> seguimiento")

    print(f"\n  Total de estudiantes con puntaje < 60: {cant_riesgo}")
    print(f"  Total derivados a seguimiento: {len(lista_seg)}")

    return lista_seg


if __name__ == "__main__":
    actividades = obtener_actividades(curso)
    total_act = len(actividades)
    estudiantes = consolidar(ids, matriz)

    print("=" * 50)
    print(" ANÁLISIS DE RENDIMIENTO Y SEGUIMIENTO")
    print("=" * 50)
    seguimiento = analizar_estudiantes(estudiantes, total_act)
