# B4 — Filtrar
puntajes = [120, 45, 300, 80, 210]

mayores_a_100 = [p for p in puntajes if p > 100]

print("Lista original intacta:", puntajes)
print("Puntajes mayores a 100:", mayores_a_100)