from dataclasses import dataclass


@dataclass
class Registro:
    id: int          # clave de la fila del estudiante en la matriz
    entregadas: int
    ptje: float
