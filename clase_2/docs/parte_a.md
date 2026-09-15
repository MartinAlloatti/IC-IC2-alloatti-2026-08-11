# A1 — Verbo correcto

| Acción | Verbo HTTP | Justificación |
|---|---|---|
| Ver la lista de libros | `GET` | Diseñado exclusivamente para solicitar y recuperar datos del servidor sin alterar su estado. |
| Agregar un libro nuevo | `POST` | Se utiliza para enviar datos al servidor y crear un nuevo recurso. |
| Borrar un libro | `DELETE` | Elimina el recurso especificado en la base de datos o servidor. |
| Cambiarle el precio a un libro | `PATCH` | Modifica de forma parcial un recurso existente, alterando únicamente el campo indicado (el precio). |
| Reemplazar un libro entero por otro | `PUT` | Reemplaza por completo el recurso existente con la nueva representación enviada en el body. |
| Cambiarle solo la disponibilidad a un libro | `PATCH` | Actualización parcial de un único campo sin tocar los demás datos. |

### Diferencia entre PUT y PATCH

- **PUT:** exige enviar el objeto completo para reemplazarlo en su totalidad. Los campos no enviados pueden quedar nulos o borrarse, dependiendo de la implementación.
- **PATCH:** modifica solo las propiedades específicas enviadas, preservando el resto de los datos del objeto.

---

# A2 — Leer códigos de estado

| Código | Significado | Ejemplo concreto (Dominio Libros) |
|---|---|---|
| **200 OK** | Petición exitosa con respuesta. | Se solicita la lista de libros con `GET /libros` y el servidor devuelve el JSON con el catálogo. |
| **201 Created** | Recurso creado exitosamente. | Se envía `POST /libros` con los datos de un libro nuevo y el servidor confirma su creación. |
| **204 No Content** | Petición exitosa sin cuerpo de respuesta. | Se ejecuta `DELETE /libros/12` y el servidor elimina el libro sin devolver contenido adicional. |
| **400 Bad Request** | Sintaxis o cuerpo de petición inválido. | El cliente envía un JSON mal formado (por ejemplo, falta una comilla) al intentar crear un libro. |
| **404 Not Found** | El recurso solicitado no existe. | Se busca `GET /libros/999` y el ID `999` no está registrado en el sistema. |
| **405 Method Not Allowed** | Verbo HTTP no soportado en la URL. | Se intenta hacer `POST /libros/12` cuando ese endpoint solo acepta `GET`, `PUT` o `DELETE`. |
| **422 Unprocessable Entity** | Error de validación de datos (Pydantic/FastAPI). | Se envía `"paginas": "doscientas"` en lugar de un número entero (`int`). |
| **500 Internal Server Error** | Error no controlado dentro del código del servidor. | Falla de conexión a la base de datos o una excepción no capturada en Python al procesar un libro. |

---

# A3 — Familias de códigos

- **2xx (Éxito):** La petición fue recibida, entendida y procesada correctamente por el servidor.
- **3xx (Redirección):** El cliente debe realizar acciones adicionales (como navegar a otra URL) para completar la solicitud.
- **4xx (Error del Cliente):** La petición contiene un error originado por el cliente, como datos inválidos, una ruta inexistente o falta de permisos.
- **5xx (Error del Servidor):** El cliente envió la petición correctamente, pero el servidor falló internamente al procesarla.

### Clasificación rápida

- `301 Moved Permanently`: implica una redirección permanente (**familia 3xx**).
- `403 Forbidden`: indica un error del cliente por falta de autorización para acceder al recurso (**familia 4xx**).

---

# A4 — JSON a mano

### Un libro individual

```json
{
  "titulo": "Fahrenheit 451",
  "autor": "Ray Bradbury",
  "paginas": 256,
  "disponible": true
}
```

### Lista de 2 libros

```json
[
  {
    "titulo": "Fahrenheit 451",
    "autor": "Ray Bradbury",
    "paginas": 256,
    "disponible": true
  },
  {
    "titulo": "Un mundo feliz",
    "autor": "Aldous Huxley",
    "paginas": 288,
    "disponible": false
  }
]
```

### Objeto con campo anidado

```json
{
  "titulo": "1984",
  "autor": "George Orwell",
  "paginas": 328,
  "disponible": true,
  "editorial": {
    "nombre": "Seix Barral",
    "pais": "España"
  }
}
```

---

# A5 — Idempotencia

### Métodos idempotentes

- `GET`
- `PUT`
- `DELETE`

### Método no idempotente

- `POST`

### ¿Por qué POST no es idempotente?

Si un cliente ejecuta `POST /libros` para crear un libro y, por una falla de red, reintenta el envío, el servidor procesará dos peticiones independientes y creará dos libros duplicados con IDs distintos.

En cambio, repetir un `PUT /libros/5` con el mismo cuerpo 100 veces dará siempre el mismo resultado: el libro con ID `5` quedará sobrescrito con los mismos datos exactos.

---

# A6 — Headers, lo mínimo

El header `Content-Type: application/json` le informa explícitamente al servidor en qué formato viene estructurado el cuerpo (*body*) del mensaje.

Si un cliente manda un body en formato JSON pero omite este header (o envía `text/plain`), el servidor podría no interpretar correctamente el texto recibido, provocando un error de validación, como un estado `400` o `422`, dependiendo de la implementación.

---

# A7 — Diseñar URLs (REST básico)

| Acción | Método y URL |
|---|---|
| Listar todos los libros | `GET /libros` |
| Ver un libro puntual | `GET /libros/{id}` |
| Listar los libros de un autor puntual | `GET /autores/{id}/libros` |
| Crear un autor | `POST /autores` |