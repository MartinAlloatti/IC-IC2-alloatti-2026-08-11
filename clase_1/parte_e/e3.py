# E3 — Reporte
import csv

peliculas = []

with open("parte_e/peliculas.csv", mode="r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        peliculas.append({
            "titulo": fila["titulo"],
            "anio": int(fila["anio"]),
            "puntaje": float(fila["puntaje"])
        })

cantidad = len(peliculas)
promedio = sum(p["puntaje"] for p in peliculas) / cantidad if cantidad > 0 else 0
mejor_pelicula = max(peliculas, key=lambda p: p["puntaje"])

print(f"Cantidad total de películas: {cantidad}")
print(f"Puntaje promedio: {promedio:.2f}")
print(f"Película mejor puntuada: {mejor_pelicula['titulo']} ({mejor_pelicula['puntaje']})")