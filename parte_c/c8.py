# C8 — Diccionario anidado
inventario = {
    "esp32": {"precio": 15000.0, "stock": 15},
    "sensor_temp": {"precio": 3200.5, "stock": 30},
    "oled_display": {"precio": 6000.0, "stock": 8},
}

# Acceso directo "de dos pisos"
precio_sensor = inventario["sensor_temp"]["precio"]

print(f"Precio del sensor de temperatura: ${precio_sensor}")