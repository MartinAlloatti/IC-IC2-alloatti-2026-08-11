# Parte D — Conceptos de MQTT

## D1 — Ver el mensaje viajar

Para verificar la comunicación Pub/Sub sin instalar nada localmente, se pueden utilizar herramientas web como el [cliente WebSocket de HiveMQ](http://www.hivemq.com/demos/websocket-client/), conectado a un broker público, por ejemplo, `broker.hivemq.com` o `test.mosquitto.org`.

1. **Suscriptor:** Abrir la pestaña o cliente 1 y suscribirse al topic `unraf/demo/saludo`.
2. **Publicador:** Abrir la pestaña o cliente 2 y publicar la carga útil `"Hola desde el publicador"` en el mismo topic: `unraf/demo/saludo`.
3. **Resultado:** El mensaje enviado por el publicador aparece instantáneamente en el panel del cliente 1.

---

## D2 — Publicar sin suscriptores

- **Publicar sin suscriptor activo:** Si el mensaje no es retenido y no hay suscriptores activos, el broker lo procesa y no lo entrega a ningún cliente. El mensaje no estará disponible para los clientes que se conecten más tarde.
- **Publicar con suscriptor activo:** El broker entrega el mensaje en tiempo real a los clientes conectados y suscritos al topic correspondiente.

> **Conclusión:** El cliente publicador desacopla su operación del receptor: publica sin necesidad de conocer quiénes son los suscriptores ni su estado.

---

## D3 — Pub/Sub vs Request/Response

### Request/Response (HTTP/REST)

Es un modelo de comunicación generalmente síncrono, donde un cliente realiza una petición a un servidor y espera una respuesta.

- El cliente debe conocer la dirección o URL del servidor.
- La comunicación se realiza mediante una solicitud y una respuesta.
- Es adecuado para operaciones puntuales que requieren una respuesta inmediata.

**Ejemplo ideal:** Consultar un historial de compras o autenticar un usuario en una base de datos.

### Publish/Subscribe (MQTT)

Es un modelo basado en eventos y generalmente asíncrono, donde los emisores y receptores se comunican mediante un broker.

- El publicador y el suscriptor no necesitan conocerse directamente.
- La comunicación está desacoplada en espacio y dirección.
- El broker se encarga de distribuir los mensajes a los suscriptores correspondientes.

**Ejemplo ideal:** Una red de 50 sensores de temperatura transmitiendo lecturas continuas a tableros de control en tiempo real.

---

## D4 — Topics y jerarquía

Para leer todos los métricos del ambiente `casa/cocina`:

- **Suscribirse a `casa/cocina/+`:** Permite recibir los topics que tienen exactamente un nivel adicional, como `temperatura` o `humedad`.
- **Suscribirse a `casa/cocina/#`:** Permite recibir todos los topics del ambiente, incluidos los subniveles anidados.

| Wildcard | Descripción | Ejemplo de coincidencia |
|---|---|---|
| **`+` (Single level)** | Reemplaza exactamente un nivel de la jerarquía. | `casa/+/temperatura` coincide con `casa/cocina/temperatura` y `casa/dormitorio/temperatura`, pero **no** con `casa/cocina/zona1/temperatura`. |
| **`#` (Multi level)** | Reemplaza múltiples niveles restantes. Debe ubicarse al final del topic. | `casa/#` coincide con `casa/cocina/temperatura`, `casa/cocina/humedad`, `casa/garaje/luces/estado`, etc. |

---

## D5 — Diseño de Topics

### Jerarquía propuesta para la vivienda

```text
<lugar>/<ambiente>/<sensor>
```

### Ejemplos

```text
casa/cocina/temperatura
casa/cocina/humedad
casa/dormitorio/temperatura
casa/dormitorio/humedad
casa/patio/temperatura
casa/patio/humedad
```

### Suscripciones

- **Suscribirse a todo:** `casa/#`
- **Suscribirse a un ambiente completo (ej. Cocina):** `casa/cocina/#`
- **Suscribirse a un tipo de sensor en cualquier ambiente (ej. Temperaturas):** `casa/+/temperatura`

---

## D6 — QoS (Quality of Service)

- **QoS 0 (At most once / Como máximo una vez):** Entrega sin confirmación (*fire and forget*). Se utiliza cuando la pérdida ocasional de un mensaje es tolerable, por ejemplo, en sensores de temperatura que transmiten cada 2 segundos.
- **QoS 1 (At least once / Al menos una vez):** Garantiza que el mensaje llegue mediante acuses de recibo, pero puede generar duplicados si se pierde la confirmación (`PUBACK`) y el mensaje se retransmite.
- **QoS 2 (Exactly once / Exactamente una vez):** Garantiza que el mensaje se procese exactamente una vez mediante un intercambio de cuatro pasos. Puede utilizarse para comandos críticos, como `"abrir la puerta"` o `"desactivar alarma"`, donde ejecutar una instrucción duplicada podría ser peligroso.

---

## D7 — Mensajes retenidos (Retained Messages)

Un mensaje publicado con la bandera `retained = True` le indica al broker MQTT que debe guardar la última carga útil enviada en ese topic.

### Diferencia con D2

A diferencia del comportamiento normal, donde un mensaje no retenido no queda disponible para nuevos suscriptores, cuando un cliente nuevo se suscribe a un topic con un mensaje retenido, el broker le envía automáticamente la **última lectura registrada**, sin esperar a que el sensor vuelva a transmitir.

### Caso de uso

Dispositivos o sensores que transmiten con baja frecuencia, por ejemplo, el estado de batería publicado cada 1 hora.

Esto permite que la aplicación cliente obtenga el estado actual del dispositivo inmediatamente al iniciar, sin tener que esperar una nueva publicación.

---

## D8 — MQTT vs Polling (Preguntar todo el tiempo)

Considerando **1.000 sensores** de puertas de acceso, donde el evento de apertura sucede **2 veces al día por sensor**:

### Escenario Polling (HTTP GET cada 1 segundo)

- **Peticiones generadas por segundo:**

  ```text
  1.000 req/seg
  ```

- **Peticiones diarias:**

  ```text
  1.000 × 86.400 = 86.400.000 peticiones/día
  ```

- **Resultado:** El servidor procesa 86,4 millones de peticiones HTTP, muchas de ellas innecesarias porque la mayoría de las respuestas indican que no hubo cambios. Esto genera un mayor consumo de CPU, ancho de banda y recursos, además de una latencia de detección de hasta 1 segundo.

### Escenario Pub/Sub (MQTT)

- Se mantienen **1.000 conexiones persistentes** con los sensores.
- El broker administra las conexiones y permanece a la espera de nuevos mensajes.
- Se procesan únicamente **2.000 mensajes al día**, suponiendo que cada sensor publica solo cuando ocurre una apertura.
- **Resultado:** Se reduce masivamente el tráfico innecesario y se obtiene una notificación prácticamente inmediata cuando ocurre el evento.

### Comparación

| Característica | Polling (HTTP) | Pub/Sub (MQTT) |
|---|---|---|
| Comunicación | El cliente pregunta periódicamente. | El broker distribuye los eventos. |
| Peticiones/mensajes | 86.400.000 peticiones diarias. | 2.000 mensajes diarios. |
| Conexión | Peticiones repetidas. | Conexiones persistentes. |
| Detección del evento | Puede tardar hasta el intervalo de consulta. | Prácticamente inmediata. |
| Eficiencia | Muchas consultas sin cambios. | Se comunica principalmente cuando hay novedades. |