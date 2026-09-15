# E4 — Filtrar y guardar
import csv

genero_buscado = "Sci-Fi"
filtradas = []

# Lectura y filtrado
with open("parte_e/peliculas.csv", mode="r", encoding="utf-8") as archivo_in:
    lector = csv.DictReader(archivo_in)
    encabezados = lector.fieldnames
    for fila in lector:
        if fila["genero"] == genero_buscado:
            filtradas.append(fila)

# Escritura en nuevo CSV
with open("parte_e/filtradas.csv", mode="w", encoding="utf-8", newline="") as archivo_out:
    escritor = csv.DictWriter(archivo_out, fieldnames=encabezados)
    escritor.writeheader()
    escritor.writerows(filtradas)

print(f"Se generó 'parte_e/filtradas.csv' con {len(filtradas)} películas del género '{genero_buscado}'.")