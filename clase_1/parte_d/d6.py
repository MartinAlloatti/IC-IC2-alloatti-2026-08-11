# D6 — Reporte combinado
def estadisticas(notas: list) -> dict:
    if not notas:
        return {"promedio": 0.0, "maximo": 0, "minimo": 0}
    return {
        "promedio": round(sum(notas) / len(notas), 2),
        "maximo": max(notas),
        "minimo": min(notas)
    }

def reporte(notas: list) -> str:
    datos = estadisticas(notas)
    return f"Promedio: {datos['promedio']} | Máximo: {datos['maximo']} | Mínimo: {datos['minimo']}"

mis_notas = [7, 8, 10, 4, 7]
print(reporte(mis_notas))