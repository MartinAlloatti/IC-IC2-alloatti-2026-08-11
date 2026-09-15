# D3 — Estadísticas
def estadisticas(notas: list) -> dict:
    if not notas:
        return {"promedio": 0.0, "maximo": None, "minimo": None}
    
    return {
        "promedio": round(sum(notas) / len(notas), 2),
        "maximo": max(notas),
        "minimo": min(notas)
    }

resultado = estadisticas([8.5, 4.0, 10.0, 6.5])
print("Estadísticas de la lista:", resultado)