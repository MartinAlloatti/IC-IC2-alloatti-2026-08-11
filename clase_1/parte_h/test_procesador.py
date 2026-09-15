import os
import pytest
from clase_1.parte_h.procesador import cargar_peliculas, calcular_estadisticas, ordenar_por_puntaje


# --- Tests para cargar_peliculas ---
def test_cargar_peliculas_exitoso():
    ruta_csv = os.path.join(os.path.dirname(__file__), "peliculas.csv")
    datos = cargar_peliculas(ruta_csv)
    assert len(datos) > 0
    assert isinstance(datos[0]["puntaje"], float)
    assert isinstance(datos[0]["anio"], int)


# --- Tests para calcular_estadisticas ---
def test_calcular_estadisticas_con_datos():
    peliculas = [
        {"titulo": "Peli A", "anio": 2020, "puntaje": 10.0, "genero": "Drama"},
        {"titulo": "Peli B", "anio": 2021, "puntaje": 6.0, "genero": "Accion"},
    ]
    res = calcular_estadisticas(peliculas)
    assert res["total"] == 2
    assert res["promedio"] == 8.0
    assert res["mejor_pelicula"] == "Peli A"


def test_calcular_estadisticas_lista_vacia():
    """Garantiza cobertura si alguien modifica la lista dejando cero elementos."""
    res = calcular_estadisticas([])
    assert res["total"] == 0
    assert res["promedio"] == 0.0
    assert res["mejor_pelicula"] is None


# --- Tests para ordenar_por_puntaje ---
def test_ordenar_por_puntaje_descendente():
    peliculas = [
        {"titulo": "B", "puntaje": 5.0},
        {"titulo": "A", "puntaje": 9.0},
    ]
    ordenadas = ordenar_por_puntaje(peliculas, descendente=True)
    assert ordenadas[0]["titulo"] == "A"
    assert ordenadas[1]["titulo"] == "B"
    assert peliculas[0]["titulo"] == "B"  # Garantiza que la lista original quede intacta


def test_ordenar_por_puntaje_ascendente():
    """Garantiza cobertura si se cambia el parámetro de ordenamiento."""
    peliculas = [
        {"titulo": "B", "puntaje": 5.0},
        {"titulo": "A", "puntaje": 9.0},
    ]
    ordenadas = ordenar_por_puntaje(peliculas, descendente=False)
    assert ordenadas[0]["titulo"] == "B"
    assert ordenadas[1]["titulo"] == "A"