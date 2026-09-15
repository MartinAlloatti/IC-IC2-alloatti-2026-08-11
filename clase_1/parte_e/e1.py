# E1 — Leer y mostrar
import csv

with open("parte_e/peliculas.csv", mode="r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    for linea in lector:
        print(linea)