# B8 — Promedio móvil
lecturas = [23.5, 24.1, 22.8, 25.0, 24.6, 23.9, 25.2, 26.0, 24.8, 23.1]
tamanio_ventana = 3

promedios_moviles = []

for i in range(len(lecturas) - tamanio_ventana + 1):
    ventana = lecturas[i : i + tamanio_ventana]
    promedio = sum(ventana) / tamanio_ventana
    promedios_moviles.append(round(promedio, 2))

print("Lecturas originales (10 elementos):", lecturas)
print("Promedios móviles (8 elementos):", promedios_moviles)