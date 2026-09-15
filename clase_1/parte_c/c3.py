# C3 — Clave que no existe
pelicula = {
    "titulo": "Inception",
    "anio": 2010,
    "director": "Christopher Nolan"
}

# Si hacemos: print(pelicula["duracion"]) -> Lanza KeyError

# Uso seguro de .get()
duracion = pelicula.get("duracion", "desconocido")
print("Duración de la película:", duracion)