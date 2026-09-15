# D1 — Encapsular
def promedio(notas: list) -> float:
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

# Pruebas con dos listas distintas
comision_a = [7.5, 8.0, 9.5, 6.0]
comision_b = [4.0, 5.5, 6.0]

print(f"Promedio Comisión A: {promedio(comision_a):.2f}")
print(f"Promedio Comisión B: {promedio(comision_b):.2f}")