# G5 — Testear el caso raro
from funciones import obtener_campo


def test_clave_inexistente_retorna_default():
    pelicula = {"titulo": "Inception", "anio": 2010}
    val = obtener_campo(pelicula, "duracion")
    assert val == "desconocido"