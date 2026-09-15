# C6 — Combinar fichas
dict1 = {"titulo": "Ford vs Ferrari", "anio": 2019}
dict2 = {"puntaje": 8, "anio": 2024}

# Combinación con el operador | (Python 3.9+)
combinado1 = dict1 | dict2  # Gana dict2
combinado2 = dict2 | dict1  # Gana dict1

print("dict1 | dict2 (Gana el año de dict2):", combinado1)
print("dict2 | dict1 (Gana el año de dict1):", combinado2)