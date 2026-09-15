import csv


def cargar_peliculas(ruta_csv: str) -> list[dict]:
    """Lee un CSV de películas y parsea sus tipos de datos."""
    peliculas = []
    with open(ruta_csv, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            peliculas.append({
                "titulo": fila["titulo"],
                "anio": int(fila["anio"]),
                "puntaje": float(fila["puntaje"]),
                "genero": fila.get("genero", "Desconocido"),
            })
    return peliculas


def calcular_estadisticas(peliculas: list[dict]) -> dict:
    """Calcula la cantidad total, el promedio y busca la película con mayor puntaje."""
    if not peliculas:
        return {"total": 0, "promedio": 0.0, "mejor_pelicula": None}

    total = len(peliculas)
    promedio = round(sum(p["puntaje"] for p in peliculas) / total, 2)
    mejor_pelicula = max(peliculas, key=lambda p: p["puntaje"])

    return {
        "total": total,
        "promedio": promedio,
        "mejor_pelicula": mejor_pelicula["titulo"],
    }


def ordenar_por_puntaje(peliculas: list[dict], descendente: bool = True) -> list[dict]:
    """Devuelve una copia de la lista de películas ordenada por puntaje."""
    return sorted(peliculas, key=lambda p: p["puntaje"], reverse=descendente)