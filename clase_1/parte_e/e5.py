# E5 — Agrupar por categoría
import csv

acumulador = {}  # {genero: {"suma": float, "cantidad": int}}

with open("parte_e/peliculas.csv", mode="r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        genero = fila["genero"]
        puntaje = float(fila["puntaje"])
        
        if genero not in acumulador:
            acumulador[genero] = {"suma": 0.0, "cantidad": 0}
            
        acumulador[genero]["suma"] += puntaje
        acumulador[genero]["cantidad"] += 1

promedios_por_genero = {
    genero: round(datos["suma"] / datos["cantidad"], 2)
    for genero, datos in acumulador.items()
}

print("Puntaje promedio por género:")
print(promedios_por_genero)