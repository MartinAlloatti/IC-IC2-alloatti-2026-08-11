# D4 — Parámetro por default
def promedio(notas: list) -> float:
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

def aprobo(notas: list, minimo: float = 6.0) -> bool:
    return promedio(notas) >= minimo

notas_evaluacion = [6.5, 6.0, 7.0]

# Prueba con valor por default (minimo=6.0)
print("Aprobó con umbral por defecto (6.0):", aprobo(notas_evaluacion))

# Prueba especificando umbral (minimo=7.0)
print("Aprobó con umbral exigente (7.0):", aprobo(notas_evaluacion, minimo=7.0))