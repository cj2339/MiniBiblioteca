def buscar_libro(biblioteca):
    titulo = input("Ingrese el título del libro que desea buscar: ")
    for libro in biblioteca:
        if libro['titulo'].lower() == titulo.lower():
            print(f"Libro encontrado: {libro['titulo']} por {libro['autor']}")
            return
    print("Libro no encontrado.")