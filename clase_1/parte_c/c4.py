# C4 — Lista de diccionarios
peliculas = [
    {"titulo": "Interstellar", "anio": 2014, "director": "Christopher Nolan"},
    {"titulo": "Atrapame si puedes", "anio": 2002, "director": "Steven Spielberg"},
    {"titulo": "Inception", "anio": 2010, "director": "Christopher Nolan"},
]

print("Lista de titulos:")
for pelicula in peliculas:
    print("-", pelicula["titulo"])