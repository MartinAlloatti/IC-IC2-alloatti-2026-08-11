# G4 — Testear un diccionario
from funciones import estadisticas


def test_estadisticas_claves_y_valores():
    datos = [8.0, 4.0, 10.0, 6.0]
    res = estadisticas(datos)

    assert "promedio" in res
    assert "maximo" in res
    assert "minimo" in res

    assert res["promedio"] == 7.0
    assert res["maximo"] == 10.0
    assert res["minimo"] == 4.0