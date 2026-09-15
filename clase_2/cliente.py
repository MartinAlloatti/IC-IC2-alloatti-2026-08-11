import sys
import requests
from requests.exceptions import ConnectionError, Timeout

BASE_URL = "http://127.0.0.1:8000"


# C8 — Uso de requests.Session para reutilizar conexiones TCP y mejorar performance
def crear_cliente_session() -> requests.Session:
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    return session


# C1, C4, C7 — GET con timeout y lectura de estados HTTP
def listar_libros(session: requests.Session) -> None:
    try:
        # C7: timeout de 5s previene bloqueos infinitos de red
        response = session.get(f"{BASE_URL}/libros", timeout=5)
        
        # C4: reaccionar según el status code
        if response.status_code == 200:
            print("OK (200) - Libros recibidos:")
            print(response.json())
        else:
            print(f"Respuesta inesperada: {response.status_code}")
    except ConnectionError: # C6: manejo explicito de falla de conexion
        print("[ERROR] No se pudo conectar con la API. ¿Servidor FastAPI levantado?")
    except Timeout: # C7: manejo explicito de timeout
        print("[ERROR] La petición superó el tiempo límite de espera (Timeout).")


# C2, C3, C4 — POST desde script
def crear_libro(session: requests.Session, libro_data: dict) -> None:
    try:
        # C3: se usa el parámetro json= que serializa automáticamente
        # y setea el header "Content-Type: application/json".
        response = session.post(f"{BASE_URL}/libros", json=libro_data, timeout=5)

        if response.status_code == 201:
            print("OK (201) - Libro creado exitosamente:")
            print(response.json())
        elif response.status_code == 422:
            print("Dato inválido (422) - Error de validación Pydantic:")
            print(response.json())
        elif response.status_code == 400:
            print("Error del cliente (400):", response.json().get("detail"))
        else:
            print(f"Estado desconocido: {response.status_code}")
    except ConnectionError:
        print("[ERROR] No se pudo conectar con la API.")


# C5 — PUT y DELETE desde el cliente
def actualizar_libro(session: requests.Session, titulo_actual: str, libro_nuevo: dict) -> None:
    try:
        response = session.put(f"{BASE_URL}/libros/{titulo_actual}", json=libro_nuevo, timeout=5)
        if response.status_code == 200:
            print(f"OK (200) - Libro '{titulo_actual}' actualizado:")
            print(response.json())
        elif response.status_code == 404:
            print(f"No existe (404) - No se encontró el libro '{titulo_actual}'")
        elif response.status_code == 422:
            print("Dato inválido (422) - Revisa el schema del body")
    except ConnectionError:
        print("[ERROR] No se pudo conectar con la API.")


def borrar_libro(session: requests.Session, titulo: str) -> None:
    try:
        response = session.delete(f"{BASE_URL}/libros/{titulo}", timeout=5)
        if response.status_code == 204:
            print(f"OK (204) - Libro '{titulo}' eliminado sin cuerpo de respuesta.")
        elif response.status_code == 404:
            print(f"No existe (404) - El libro '{titulo}' no existe.")
    except ConnectionError:
        print("[ERROR] No se pudo conectar con la API.")


# C7 — Provocar un Timeout garantizado
def probar_timeout_forzado():
    print("\n--- Probando Timeout con IP no enrutable ---")
    try:
        # IP no enrutable (bloque 10.255.255.1) obliga a agotar los 1s de espera
        requests.get("http://10.255.255.1/", timeout=1)
    except Timeout:
        print("OK: Se capturó correctamente la excepción 'requests.exceptions.Timeout'.")


if __name__ == "__main__":
    cliente = crear_cliente_session()

    print("--- 1. Listar Libros ---")
    listar_libros(cliente)

    print("\n--- 2. Crear Libro ---")
    nuevo = {
        "titulo": "El Aleph",
        "paginas": 146,
        "disponible": True,
        "editorial": {"nombre": "Losada", "pais": "Argentina"},
    }
    crear_libro(cliente, nuevo)

    print("\n--- 3. Listar para verificar POST ---")
    listar_libros(cliente)

    print("\n--- 4. Actualizar Libro (PUT) ---")
    actualizado = {
        "titulo": "El Aleph",
        "paginas": 160,
        "disponible": False,
        "editorial": {"nombre": "Emecé", "pais": "Argentina"},
    }
    actualizar_libro(cliente, "El Aleph", actualizado)

    print("\n--- 5. Borrar Libro (DELETE) ---")
    borrar_libro(cliente, "El Aleph")

    print("\n--- 6. Verificar 404 en GET posterior al borrado ---")
    actualizar_libro(cliente, "El Aleph", actualizado)

    # Prueba de timeout
    probar_timeout_forzado()