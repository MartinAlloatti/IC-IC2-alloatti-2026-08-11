# G1 — Tu primer test
from funciones import promedio


def test_promedio_basico():
    resultado = promedio([7, 4, 9, 10, 6])
    assert resultado == 7.2