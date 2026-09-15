# Notas Conceptuales: MQTT vs HTTP (Polling)

## ¿Qué es el modelo Publicador/Suscriptor (Pub/Sub)?
En el modelo Pub/Sub, la persona o dispositivo que envía información (publicador) no habla directamente con quien la recibe (suscriptor). El publicador simplemente emite un mensaje etiquetado con un tema ("topic") y se desentiende. Los clientes interesados se anotan a ese tema para recibir de forma automática cualquier dato nuevo.

## ¿Qué es un Broker?
Es el servidor central o intermediario encargado de gestionar la mensajería. Su única tarea es recibir los mensajes que envían los publicadores, filtrar cuáles clientes están suscriptos a cada topic, y distribuirlos en tiempo real. Si no hay suscriptores escuchando, el broker descarta el mensaje (salvo que sea un mensaje *retained*).

## Topics y Wildcards
Un **topic** es una ruta en forma de texto separada por barras (ej. `casa/cocina/temperatura`) que actúa como la dirección del mensaje.

Los **wildcards** son comodines para suscribirse a varios topics a la vez:
* `+` **(Single-level):** Reemplaza un único nivel. `casa/+/temperatura` escucha la temperatura de la cocina, dormitorio, etc., pero no subniveles más profundos.
* `#` **(Multi-level):** Reemplaza todos los subniveles restantes. `casa/cocina/#` escucha todo lo que ocurra dentro de la cocina (temperatura, humedad, luz).

## ¿Por qué MQTT escala mejor que el Polling para IoT?
Hacer *polling* significa que 1.000 sensores le pregunten a un servidor HTTP cada 1 segundo "¿hay datos nuevos?". Esto genera 86,4 millones de peticiones diarias, consumiendo procesador y ancho de banda aunque la temperatura no haya cambiado. 

Con **MQTT**, los sensores mantienen un canal liviano abierto con el broker y **solo transmiten cuando ocurre un evento o cambio significativo**. La carga del servidor cae drásticamente y las notificaciones llegan al instante (en milisegundos).