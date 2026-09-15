# G3 — Varios casos, varios tests
from funciones import aprobo


def test_aprobo_caso_exitoso():
    assert aprobo([8, 7, 9]) is True


def test_aprobo_caso_reprobado():
    assert aprobo([4, 5, 3]) is False


def test_aprobo_caso_limite():
    # Promedio exactamente 6.0
    assert aprobo([6, 6, 6]) is True