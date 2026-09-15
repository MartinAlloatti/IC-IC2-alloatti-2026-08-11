# IC-IC2-alloatti-2026-08-11
# IC2 — Bloque de Software: Ejercicios Individuales

Repositorio individual correspondiente al **Bloque de Software** de la materia *Ingeniería en Computación 2* (Universidad Nacional de Rafaela).

**Alumno:** Martín Alloatti  
**Legajo / Repo:** `IC-IC2-alloatti-2026-08-11`

---

## Requisitos Previos e Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/MartinAlloatti/IC-IC2-alloatti-2026-08-11.git
cd IC-IC2-alloatti-2026-08-11
```

### 2. Crear y activar el entorno virtual (`.venv`)

```bash
python -m venv .venv
```

**En Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**En Windows (Git Bash):**

```bash
source .venv/Scripts/activate
```

### 3. Instalar dependencias del proyecto

```bash
pip install pytest fastapi uvicorn requests httpx
```

---

## Estructura del Repositorio

El proyecto está organizado de manera modular por clases y carpetas temáticas.

### `clase_1/` — Fundamentos de Python, Testing y Git

- **`parte_a/`** — Conceptos básicos de Python y estructuras de control.
- **`parte_b/`** — Manejo de listas, slicing, filtrado y promedios móviles.
- **`parte_c/`** — Diccionarios, búsquedas, combinaciones y estructuras anidadas.
- **`parte_d/`** — Funciones, parámetros por defecto, modularización y casos borde.
- **`parte_e/`** — Lectura, escritura, filtrado y agrupación sobre archivos CSV.
- **`parte_f/`** — Documentación y simulación de flujos de trabajo en Git/GitHub.
- **`parte_g/`** — Pruebas unitarias automáticas con `pytest` y `@pytest.mark.parametrize`.
- **`parte_h/`** — Mini-proyecto integrador (CSV, estadísticas, ordenamiento y tests).

### `clase_2/` — APIs RESTful (FastAPI) y Conceptos de MQTT

- **`main.py`** — API RESTful con FastAPI (endpoints para libros y autores, validaciones con Pydantic y filtros query).
- **`cliente.py`** — Cliente HTTP con `requests.Session`, manejo de status codes, timeouts y reintentos.
- **`test_main.py`** — Suite de tests de integración para la API usando `TestClient` y `pytest`.
- **`docs/`** — Documentación conceptual sobre HTTP, verbos, idempotencia y fundamentos de MQTT (Pub/Sub, broker, topics, wildcards y QoS).

---

## Ejecución de Scripts y Servidores

### Clase 1

Para ejecutar el mini-proyecto integrador de la Parte H:

```bash
python clase_1/parte_h/main.py
```

### Clase 2 (API & Cliente)

#### 1. Levantar la API con Uvicorn

```bash
uvicorn clase_2.main:app --reload
```

- **URL local:** `http://127.0.0.1:8000`
- **Documentación interactiva (Swagger):** `http://127.0.0.1:8000/docs`

#### 2. Ejecutar el cliente HTTP

En otra terminal, con el entorno virtual activado:

```bash
python clase_2/cliente.py
```

---

## Ejecución de Tests (`pytest`)

Para correr **todos los tests** del repositorio (Clase 1 y Clase 2):

```bash
python -m pytest
```

Para correr únicamente los tests de una carpeta específica:

```bash
# Tests de Clase 1
python -m pytest clase_1/parte_g/
python -m pytest clase_1/parte_h/

# Tests de la API (Clase 2)
python -m pytest clase_2/test_main.py
```

---

## F3 — Documentación de Errores de Contrato

### 1. Error de Validación en la API (`422 Unprocessable Entity`)

- **Causa:** Enviar un `POST /libros` omitiendo el campo obligatorio `paginas` o enviando un tipo no numérico (por ejemplo, `"paginas": "muchas"`).
- **Mensaje real observado:**

```json
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": ["body", "paginas"],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "muchas"
    }
  ]
}
```

### 2. Error de Recurso No Encontrado en el Cliente (`404 Not Found`)

- **Causa:** Intentar actualizar o consultar mediante `GET`, `PUT` o `DELETE` un título inexistente (por ejemplo, `/libros/Inexistente`).
- **Mensaje real observado:**

```json
{
  "detail": "El libro 'Inexistente' no fue encontrado."
}
```

### 3. Error de Conexión en el Cliente (API apagada)

- **Causa:** Ejecutar `python clase_2/cliente.py` sin haber iniciado el servidor Uvicorn.
- **Excepción real capturada:** `requests.exceptions.ConnectionError`
- **Mensaje real en consola:**

```text
[ERROR] No se pudo conectar con la API. ¿Servidor FastAPI levantado?
```

---

## F4 — Comparativa: Swagger (`/docs`) vs. cURL / Postman

### Similitudes

Ambas herramientas permiten realizar peticiones HTTP reales al servidor FastAPI, procesando encabezados, cuerpos JSON y devolviendo los códigos de estado correspondientes, como `200`, `201`, `422` y `404`.

### Diferencias

- **Swagger (`/docs`):** Se genera automáticamente a partir del código de FastAPI/Pydantic. Es ideal durante la fase de desarrollo para probar rápida y visualmente los endpoints sin configurar herramientas externas.
- **cURL / Postman:** Permiten guardar colecciones de peticiones reutilizables, automatizar pruebas integrales, configurar variables de entorno (como tokens de autenticación) y compartir flujos completos de API con otros desarrolladores.