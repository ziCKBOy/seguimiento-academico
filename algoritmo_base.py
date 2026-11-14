# Algoritmo base y nuevo requerimiento (secciones 5 y 6 del informe).
# Usa los mismos datos y funciones de apoyo de propuestaB.py.
from propuestaB import ids, matriz, curso, obtener_actividades, consolidar


# 5. Procesamiento de información (Algoritmo base)
def analizar_rendimiento(estudiantes):
    """Recorre todos los estudiantes, alerta los puntajes < 60 y muestra el total en riesgo."""
    cant_riesgo = 0

    for est in estudiantes:
        if est.ptje < 60:
            cant_riesgo = cant_riesgo + 1
            print(f"  [ALERTA]   {est.id} | puntaje: {est.ptje:>3} | bajo 60")

    print(f"\n  Total de estudiantes con puntaje < 60: {cant_riesgo}")


# 6. Resolución de nuevos requerimientos (Propuesta B)
def detectar_seguimiento(estudiantes, total_act):
    """Retorna los IDs con puntaje < 60 y entregas < 70 % en un solo recorrido."""
    lista_seg = []

    for est in estudiantes:
        pct_ent = (est.entregadas / total_act) * 100

        if (est.ptje < 60) and (pct_ent < 70.0):
            lista_seg.append(est.id)
            print(f"  [DERIVADO] {est.id} -> seguimiento")

    return lista_seg


if __name__ == "__main__":
    actividades = obtener_actividades(curso)
    total_act = len(actividades)
    estudiantes = consolidar(ids, matriz)

    print("=" * 50)
    print(" ALGORITMO BASE Y NUEVO REQUERIMIENTO")
    print("=" * 50)
    analizar_rendimiento(estudiantes)
    seguimiento = detectar_seguimiento(estudiantes, total_act)
    print(f"\n  Total derivados a seguimiento: {len(seguimiento)}")
