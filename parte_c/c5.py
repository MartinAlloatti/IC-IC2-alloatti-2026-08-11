# C5 — Búsqueda
peliculas = [
    {"titulo": "Interstellar", "anio": 2014, "director": "Christopher Nolan"},
    {"titulo": "Atrapame si puedes", "anio": 2002, "director": "Steven Spielberg"},
    {"titulo": "Inception", "anio": 2010, "director": "Christopher Nolan"},
]

director_buscado = "Nolan"
encontradas = []

for pelicula in peliculas:
    # Opción (b): Coincidencia parcial con 'in'
    if director_buscado.lower() in pelicula["director"].lower():
        encontradas.append(pelicula)

if encontradas:
    print(f"Películas encontradas para '{director_buscado}':")
    for p in encontradas:
        print(f"- {p['titulo']} ({p['anio']})")
else:
    print(f"No se encontraron películas del director '{director_buscado}'.")