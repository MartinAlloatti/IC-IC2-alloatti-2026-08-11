# B3 — El mas alto y el mas bajo
puntajes = [120, 45, 300, 80, 210]

# Solución con for
mayor = puntajes[0]
menor = puntajes[0]
suma  = 0

for p in puntajes:
    if p > mayor:
        mayor = p
    if p < menor:
        menor = p
    suma += p

promedio = suma / len(puntajes)

print(f"[con for] Mayor: {mayor}, Menor: {menor}, Promedio: {promedio:.2f}")

# Verificacion con funciones nativas 
mayor_fun    = max(puntajes)
menor_fun    = min(puntajes)
promedio_fun = sum(puntajes) / len(puntajes)

print(f"[con funciones] Mayor: {mayor_fun}, Menor: {menor_fun}, Promedio: {promedio_fun:.2f}")