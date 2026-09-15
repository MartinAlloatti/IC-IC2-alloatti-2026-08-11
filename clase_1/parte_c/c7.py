# C7 — Contador de palabras
frase = "mqtt y apis en contenedores con python y docker para apis"

palabras = frase.lower().split()
conteo = {}

for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

print("Conteo de apariciones por palabra:")
print(conteo)