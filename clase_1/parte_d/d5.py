# D5 — Que no explote con la lista vacía
def promedio(notas: list) -> float:
    # Se decide devolver 0.0 para evitar ZeroDivisionError sin detener la ejecución
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

# Prueba de control de excepción implícita
lista_vacia = []
resultado = promedio(lista_vacia)

print("Promedio de lista vacía:", resultado)