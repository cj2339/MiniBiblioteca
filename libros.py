class Libros:
	def __init__(self, id, nombre, autor, editorial):
		self.id = id
		self.nombre = nombre
		self.autor = autor
		self.editorial = editorial

	def __str__(self):
		return f"{self.id}-> {self.nombre}: Escrito por {self.autor} y publicado por la editorial {self.editorial}"

	@property
	def get_id(self):
		return self.id

	@property
	def get_nombre(self):
		return self.nombre

	@property
	def get_autor(self):
		return self.autor

	@property
	def get_editorial(self):
		return self.editorial

	def crear(lista_libros):
		id = 0
		nombre = input("Introduce el nombre del libro: ")
		autor = input("Introduce el nombre del autor: ")
		editorial = input("Introduce el nombre de la editorial: ")

		if lista_libros:
			id = lista_libros[-1].get_id + 1

		libro = Libros(id,nombre, autor, editorial)
		lista_libros.append(libro)

	def listar(lista_libros):
		print("\n--- LIBROS ---")
		if lista_libros:
			for libro in lista_libros:
				print(libro)
		else:
			print("No hay libros registrados.")