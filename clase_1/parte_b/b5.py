# B5 — Ranking
puntajes = [120, 45, 300, 80, 210]

# Opcion 1: Obtener una copia ordenada sin modificar la original
ranking_copia = sorted(puntajes, reverse=True)
print("Copia ordenada (sorted):", ranking_copia)
print("Original sigue igual:", puntajes)

# Opcion 2: Ordenar la lista directamente en su lugar (modifica la variable original)
puntajes.sort(reverse=True)
print("Lista ordenada in-place (.sort()):", puntajes)