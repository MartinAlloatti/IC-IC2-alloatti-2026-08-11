from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="API de Libros y Autores")


# --- MODELOS (Pydantic) ---

class Editorial(BaseModel):
    nombre: str
    pais: str


class Libro(BaseModel):
    titulo: str
    paginas: int = Field(gt=0, description="Las páginas deben ser un entero mayor a 0")
    disponible: bool = True
    editorial: Editorial | None = None


class LibroOut(BaseModel):
    """Ejemplo para response_model (B12): explaya el filtrado de campos de salida."""
    titulo: str
    paginas: int
    disponible: bool


class Autor(BaseModel):
    nombre: str
    nacionalidad: str


# --- BASE DE DATOS EN MEMORIA ---

db_libros: list[dict] = [
    {
        "titulo": "Fahrenheit 451",
        "paginas": 256,
        "disponible": True,
        "editorial": {"nombre": "Minotauro", "pais": "Argentina"},
    },
    {
        "titulo": "1984",
        "paginas": 328,
        "disponible": False,
        "editorial": {"nombre": "Seix Barral", "pais": "España"},
    },
    {
        "titulo": "Un mundo feliz",
        "paginas": 288,
        "disponible": True,
        "editorial": {"nombre": "Plaza & Janes", "pais": "España"},
    },
]

db_autores: list[dict] = [
    {"nombre": "Ray Bradbury", "nacionalidad": "Estadounidense"},
    {"nombre": "George Orwell", "nacionalidad": "Británica"},
]


# --- ENDPOINTS ---

# B1 — Endpoint que saluda
@app.get("/")
def home():
    return {"mensaje": "hola"}


# B2 & B11 — Listar libros con filtro opcional query param (paginas_min)
@app.get("/libros", response_model=list[Libro])
def listar_libros(paginas_min: int | None = None):
    if paginas_min is not None:
        return [l for l in db_libros if l["paginas"] >= paginas_min]
    return db_libros


# B3, B8, B10 & B12 — Crear libro con validación (gt=0) y valores por defecto
@app.post("/libros", status_code=status.HTTP_201_CREATED, response_model=Libro)
def crear_libro(libro: Libro):
    # Verificación de duplicados por título
    if any(l["titulo"].lower() == libro.titulo.lower() for l in db_libros):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un libro registrado con ese título.",
        )
    nuevo_libro = libro.model_dump()
    db_libros.append(nuevo_libro)
    return nuevo_libro


# B5 — Buscar uno por título
@app.get("/libros/{titulo}", response_model=Libro)
def obtener_libro(titulo: str):
    for libro in db_libros:
        if libro["titulo"].lower() == titulo.lower():
            return libro
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"El libro '{titulo}' no fue encontrado.",
    )


# B6 — Actualizar (PUT completo)
@app.put("/libros/{titulo}", response_model=Libro)
def actualizar_libro(titulo: str, libro_nuevo: Libro):
    for i, libro in enumerate(db_libros):
        if libro["titulo"].lower() == titulo.lower():
            db_libros[i] = libro_nuevo.model_dump()
            return db_libros[i]
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"No se puede actualizar. El libro '{titulo}' no existe.",
    )


# B7 — Borrar (DELETE)
@app.delete("/libros/{titulo}", status_code=status.HTTP_204_NO_CONTENT)
def borrar_libro(titulo: str):
    for i, libro in enumerate(db_libros):
        if libro["titulo"].lower() == titulo.lower():
            db_libros.pop(i)
            # 204 No Content NO devuelve cuerpo (body). Se usa para confirmar eliminaciones exitosas.
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"No se puede borrar. El libro '{titulo}' no existe.",
    )


# B9 — Segundo recurso independiente (/autores)
@app.get("/autores", response_model=list[Autor])
def listar_autores():
    return db_autores


@app.post("/autores", status_code=status.HTTP_201_CREATED, response_model=Autor)
def crear_autor(autor: Autor):
    nuevo_autor = autor.model_dump()
    db_autores.append(nuevo_autor)
    return nuevo_autor