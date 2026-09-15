def promedio(notas: list) -> float:
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


def aprobo(notas: list, minimo: float = 6.0) -> bool:
    return promedio(notas) >= minimo


def estadisticas(notas: list) -> dict:
    if not notas:
        return {"promedio": 0.0, "maximo": None, "minimo": None}
    return {
        "promedio": round(sum(notas) / len(notas), 2),
        "maximo": max(notas),
        "minimo": min(notas),
    }


def obtener_campo(diccionario: dict, clave: str, default="desconocido"):
    return diccionario.get(clave, default)