# D2 — Aprobo?
def promedio(notas: list) -> float:
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

def aprobo(notas: list) -> bool:
    # Utiliza promedio() por dentro
    return promedio(notas) >= 6.0

alumno_1 = [8.0, 7.0, 6.5]
alumno_2 = [4.0, 5.0, 5.5]

print("Alumno 1 aprobo:", aprobo(alumno_1))
print("Alumno 2 aprobo:", aprobo(alumno_2))