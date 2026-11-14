# Propuesta A (Parte 5 del enunciado): tres procesamientos separados, 3n iteraciones.
#   1.er recorrido: estudiantes con puntaje < 60
#   2.º recorrido:  estudiantes con entregas < 70 %
#   3.er procesamiento: estudiantes que aparecen en ambos grupos
# Cada recorrido marca a los estudiantes en un arreglo paralelo (índice i = estudiante i),
# de modo que el tercer procesamiento es otra pasada de n elementos, sin búsquedas anidadas.
# Usa los mismos datos y funciones de apoyo de propuestaB.py.
from propuestaB import ids, matriz, curso, obtener_actividades, consolidar


def grupo_puntaje(estudiantes):
    """1.er recorrido: marca a los estudiantes con puntaje < 60."""
    marcas = [False] * len(estudiantes)

    for i in range(len(estudiantes)):
        if estudiantes[i].ptje < 60:
            marcas[i] = True

    return marcas


def grupo_entregas(estudiantes, total_act):
    """2.º recorrido: marca a los estudiantes con entregas < 70 %."""
    marcas = [False] * len(estudiantes)

    for i in range(len(estudiantes)):
        pct_ent = (estudiantes[i].entregadas / total_act) * 100
        if pct_ent < 70.0:
            marcas[i] = True

    return marcas


def interseccion(estudiantes, marcas_puntaje, marcas_entregas):
    """3.er procesamiento: retorna los IDs que están en ambos grupos."""
    lista_seg = []

    for i in range(len(estudiantes)):
        if marcas_puntaje[i] and marcas_entregas[i]:
            lista_seg.append(estudiantes[i].id)
            print(f"  [DERIVADO] {estudiantes[i].id} -> seguimiento")

    return lista_seg


if __name__ == "__main__":
    actividades = obtener_actividades(curso)
    total_act = len(actividades)
    estudiantes = consolidar(ids, matriz)

    print("=" * 50)
    print(" PROPUESTA A: TRES PROCESAMIENTOS")
    print("=" * 50)
    marcas_puntaje = grupo_puntaje(estudiantes)
    marcas_entregas = grupo_entregas(estudiantes, total_act)
    seguimiento = interseccion(estudiantes, marcas_puntaje, marcas_entregas)
    print(f"\n  Total derivados a seguimiento: {len(seguimiento)}")
