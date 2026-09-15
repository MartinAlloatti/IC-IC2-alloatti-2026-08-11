import os
from clase_1.parte_h.procesador import cargar_peliculas, calcular_estadisticas, ordenar_por_puntaje


def main():
    ruta_csv = os.path.join(os.path.dirname(__file__), "peliculas.csv")
    
    # 1. Leer datos
    peliculas = cargar_peliculas(ruta_csv)
    
    # 2. Calcular estadísticas
    stats = calcular_estadisticas(peliculas)
    
    # 3. Ordenar películas
    peliculas_ordenadas = ordenar_por_puntaje(peliculas)

    # Impresión del reporte
    print("=" * 45)
    print("       REPORTE DE PELÍCULAS E INTEGRACIÓN")
    print("=" * 45)
    print(f"Total de películas:     {stats['total']}")
    print(f"Puntaje promedio:       {stats['promedio']}")
    print(f"Mejor película:         {stats['mejor_pelicula']}")
    print("-" * 45)
    print("Ranking por puntaje (descendente):")
    for p in peliculas_ordenadas:
        print(f"  - [{p['puntaje']}] {p['titulo']} ({p['anio']}) | {p['genero']}")
    print("=" * 45)


if __name__ == "__main__":
    main()