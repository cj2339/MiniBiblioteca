import csv
import os

from libros import Libros

ARCHIVO = "libros.txt"


def guardar_libros(biblioteca):
    """Guarda todos los libros de la biblioteca en libros.txt (un libro por línea)."""
    with open(ARCHIVO, "w", encoding="utf-8", newline="") as f:
        escritor = csv.writer(f, delimiter=";")
        for libro in biblioteca:
            if isinstance(libro, dict):
                # Por si alguien pasa diccionarios (como en la prueba de la ficha)
                escritor.writerow([
                    libro.get("id", ""),
                    libro.get("titulo", libro.get("nombre", "")),
                    libro.get("autor", ""),
                    libro.get("anio", libro.get("editorial", "")),
                ])
            else:
                escritor.writerow([libro.id, libro.nombre, libro.autor, libro.editorial])
    print(f"Se han guardado {len(biblioteca)} libro(s) en {ARCHIVO}.")


def cargar_libros():
    """Lee libros.txt y devuelve la lista de libros. Si no existe, devuelve []."""
    if not os.path.exists(ARCHIVO):
        return []

    biblioteca = []
    with open(ARCHIVO, "r", encoding="utf-8", newline="") as f:
        lector = csv.reader(f, delimiter=";")
        for fila in lector:
            if len(fila) != 4:
                continue  # línea vacía o mal formada
            id_libro, nombre, autor, editorial = fila
            try:
                id_libro = int(id_libro)
            except ValueError:
                id_libro = len(biblioteca)
            biblioteca.append(Libros(id_libro, nombre, autor, editorial))
    return biblioteca
