from modelos import Registro

###################################################################################
#DEFINICIONES
# Lista de estudiantes: cada entero es el identificador de una fila de la matriz.
ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Matriz bidimensional indexada por identificador: matriz[id] -> fila del estudiante.
# Cada fila: una celda por actividad (mismo orden que obtener_actividades(curso)).
# Cada celda: (puntaje obtenido, True si fue entregada / False si no).
matriz = {
    1:  [(10, True),  (15, True),  (20, True),  (0, False),  (0, False)],
    2:  [(20, True),  (25, True),  (10, True),  (0, False),  (0, False)],
    3:  [(30, True),  (30, True),  (20, True),  (0, False),  (0, False)],
    4:  [(20, True),  (20, True),  (20, True),  (20, True),  (10, True)],
    5:  [(15, True),  (10, True),  (0, False),  (0, False),  (0, False)],
    6:  [(25, True),  (30, True),  (25, True),  (20, True),  (15, True)],
    7:  [(10, True),  (0, False),  (15, True),  (0, False),  (0, False)],
    8:  [(30, True),  (25, True),  (30, True),  (25, True),  (0, False)],
    9:  [(5,  True),  (10, True),  (0, False),  (0, False),  (0, False)],
    10: [(20, True),  (20, True),  (20, True),  (15, True),  (10, True)],
}

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
    """Por cada id de la lista busca su fila en la matriz y arma un Registro con puntaje total y entregas."""
    lista_est = []
    for id_est in lista_ids:
        fila = tabla[id_est]
        puntaje = 0
        entregadas = 0
        for pts, entregada in fila:
            puntaje += pts
            if entregada:
                entregadas += 1
        lista_est.append(Registro(id_est, entregadas, puntaje))
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
