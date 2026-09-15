# G7 — Un solo test, varios casos (parametrize)
import pytest
from funciones import aprobo


@pytest.mark.parametrize(
    "notas, esperado",
    [
        ([8, 7, 9], True),   # Caso aprueba
        ([4, 5, 3], False),  # Caso no aprueba
        ([6, 6, 6], True),   # Caso límite
    ],
)
def test_aprobo_parametrizado(notas, esperado):
    assert aprobo(notas) == esperado