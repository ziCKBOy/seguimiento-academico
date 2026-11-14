# Algoritmo base (sección 5 del informe): un solo recorrido que alerta los puntajes < 60
# y muestra el total en riesgo. El nuevo requerimiento (sección 6) se incorpora a esta
# misma función en propuestaB.py. Usa los mismos datos y funciones de apoyo de propuestaB.py.
from propuestaB import ids, matriz, consolidar


# 5. Procesamiento de información (Algoritmo base)
def analizar_estudiantes(estudiantes):
    """Recorre todos los estudiantes una sola vez: alerta puntaje < 60 y muestra el total en riesgo."""
    cant_riesgo = 0

    for est in estudiantes:
        if est.ptje < 60:
            cant_riesgo = cant_riesgo + 1
            print(f"  [ALERTA]   {est.id} | puntaje: {est.ptje:>3} | bajo 60")

    print(f"\n  Total de estudiantes con puntaje < 60: {cant_riesgo}")


if __name__ == "__main__":
    estudiantes = consolidar(ids, matriz)

    print("=" * 50)
    print(" ALGORITMO BASE")
    print("=" * 50)
    analizar_estudiantes(estudiantes)
