import pytest
from fastapi.testclient import TestClient
from clase_2.main import app, db_libros

client = TestClient(app)


# Fixture para limpiar o reiniciar el estado de la lista de libros antes de cada test
@pytest.fixture(autouse=True)
def reset_db_libros():
    db_libros.clear()
    db_libros.extend([
        {
            "titulo": "Fahrenheit 451",
            "paginas": 256,
            "disponible": True,
            "editorial": {"nombre": "Minotauro", "pais": "Argentina"},
        },
        {
            "titulo": "1984",
            "paginas": 328,
            "disponible": False,
            "editorial": {"nombre": "Seix Barral", "pais": "España"},
        },
    ])


# --- E1 — Tu primer test de API ---
def test_listar_libros_status_200():
    response = client.get("/libros")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# --- E2 — Automatizá el 422 de B4 ---
def test_crear_libro_inválido_sin_paginas():
    # Falta el campo obligatorio 'paginas'
    libro_invalido = {"titulo": "Libro Incompleto"}
    response = client.post("/libros", json=libro_invalido)
    assert response.status_code == 422
    assert "paginas" in str(response.json()["detail"])


def test_crear_libro_inválido_tipo_incorrecto():
    # Se envía 'paginas' como string en vez de int
    libro_invalido = {"titulo": "Libro Erroneo", "paginas": "muchas"}
    response = client.post("/libros", json=libro_invalido)
    assert response.status_code == 422


# --- E3 — Camino feliz y camino con error ---
def test_crear_libro_camino_feliz():
    nuevo_libro = {
        "titulo": "Rayuela",
        "paginas": 600,
        "disponible": True,
        "editorial": {"nombre": "Sudamericana", "pais": "Argentina"},
    }
    response = client.post("/libros", json=nuevo_libro)
    assert response.status_code == 201
    datos = response.json()
    assert datos["titulo"] == "Rayuela"
    assert datos["paginas"] == 600


def test_crear_libro_camino_error_paginas_invalidas():
    # El campo paginas debe ser gt=0 segun la validacion del modelo
    libro_invalido = {"titulo": "Libro Cero", "paginas": 0}
    response = client.post("/libros", json=libro_invalido)
    assert response.status_code == 422


# --- E4 — Testear la secuencia POST → GET ---
def test_secuencia_post_luego_get():
    libro = {
        "titulo": "El Hacedor",
        "paginas": 160,
        "disponible": True,
    }

    # 1. Hacemos el POST del libro nuevo
    res_post = client.post("/libros", json=libro)
    assert res_post.status_code == 201

    # 2. Hacemos el GET y verificamos que el libro figure en la lista devuelta
    res_get = client.get("/libros")
    assert res_get.status_code == 200
    titulos = [l["titulo"] for l in res_get.json()]
    assert "El Hacedor" in titulos