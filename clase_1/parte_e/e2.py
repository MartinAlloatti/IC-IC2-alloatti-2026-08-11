# E2 — Cuidado: todo viene como texto
import csv

suma_puntajes = 0.0

with open("parte_e/peliculas.csv", mode="r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        # Los datos leídos de un CSV son siempre str, por lo que es necesario castear a float
        suma_puntajes += float(fila["puntaje"])

print(f"Suma total de puntajes: {suma_puntajes:.2f}")