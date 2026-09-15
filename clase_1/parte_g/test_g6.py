# G6 — El caso límite que decidiste en D5
from clase_1.parte_g.funciones import promedio


def test_promedio_lista_vacia_devuelve_cero():
    # Confirma que la decisión tomada para evitar ZeroDivisionError devuelve 0.0
    assert promedio([]) == 0.0