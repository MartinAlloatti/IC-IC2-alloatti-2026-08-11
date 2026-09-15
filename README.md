# IC-IC2-alloatti-2026-08-11
# IC2 — Bloque de Software: Ejercicios Individuales

Repositorio individual correspondiente al **Bloque de Software** de la materia *Ingeniería en Computación 2* (Universidad Nacional de Rafaela).

**Alumno:** Martín Alloatti  
**Legajo / Repo:** `IC-IC2-alloatti-2026-08-11`

---

## Requisitos Previos e Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/MartinAlloatti/IC-IC2-alloatti-2026-08-11.git](https://github.com/MartinAlloatti/IC-IC2-alloatti-2026-08-11.git)
   cd IC-IC2-alloatti-2026-08-11
Crear y activar el entorno virtual (venv):

Bash
python -m venv .venv

# En Windows (Git Bash / CMD / PowerShell):
source .venv/Scripts/activate   # Bash
# .venv\Scripts\activate.bat   # CMD
Instalar dependencias de desarrollo:

Bash
pip install pytest

# Estructura del Repositorio
El proyecto está organizado por carpetas temáticas que corresponden a las distintas partes del bloque de software:

parte_a/ — Conceptos básicos de Python y estructuras de control.

parte_b/ — Manejo de listas, slicing, filtrado y promedios móviles.

parte_c/ — Diccionarios, búsquedas, combinaciones (.update() / |) y estructuras anidadas.

parte_d/ — Funciones, parámetros por defecto, modularización y manejo de casos bordes.

parte_e/ — Lectura, escritura, filtrado y agrupación sobre archivos CSV (peliculas.csv).

parte_f/ — Documentación y simulación de flujos de trabajo en Git/GitHub (ramas, PRs, merge, stash y resolución de conflictos).

parte_g/ — Pruebas unitarias automáticas con pytest y test parametrizados (@pytest.mark.parametrize).

parte_h/ — Mini-proyecto integrador que combina lectura CSV, funciones de estadísticas, ordenamiento y tests de cobertura.

# Ejecución de Scripts
Para ejecutar el mini-proyecto integrador de la Parte H, corré desde la raíz del repo:

Bash
python parte_h/main.py
Para ejecutar cualquier script individual de las partes anteriores (por ejemplo, de la Parte C o E):

Bash
python parte_c/c1_ficha.py
python parte_e/e3_reporte_csv.py

# Ejecución de Tests (pytest)
Para correr toda la suite de pruebas unitarias automáticas (Partes G y H) y verificar que todos los casos den en verde (passed), ejecutá:

Bash
python -m pytest
Para correr únicamente los tests de una carpeta en específico:

Bash
python -m pytest parte_g/
python -m pytest parte_h/