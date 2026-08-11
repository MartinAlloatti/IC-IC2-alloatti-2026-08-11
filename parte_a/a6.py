# par o impar con el resto

pares = 0
impares = 0

for i in range(1, 31):
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Total: {pares + impares}")
