# encadenacion de conversiones de unidades

km = 10

kmAmillas = 0.621371
millasApies = 5280

millas = km * kmAmillas
pies = millas * millasApies

print(f"Distancia inicial: {km} km")
print(f"Distancia en millas: {millas} millas")
print(f"Distancia en pies: {pies} ft")
