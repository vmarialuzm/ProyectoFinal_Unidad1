from tabulate import tabulate

class Libro:
    def __init__(self, id, titulo, genero, ISBN, editorial, autores):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN
        self.editorial = editorial
        self.autores = autores

    def __repr__(self):
        return f"Libro({self.id}, {self.titulo}, {self.genero}, {self.ISBN}, {self.editorial}, {self.autores})"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def leer_archivo(self, archivo):
        with open(archivo, "r") as f:
            for linea in f:
                id, titulo, genero, ISBN, editorial, autores = linea.strip().split(",")
                autores = autores.split(";")
                libro = Libro(id, titulo, genero, ISBN, editorial, autores)
                self.libros.append(libro)

    def listar_libros(self):
        headers = ["ID", "Título", "Género", "ISBN", "Editorial", "Autores"]
        data = [[libro.id, libro.titulo, libro.genero, libro.ISBN, libro.editorial, "; ".join(libro.autores)] for libro in self.libros]
        print(tabulate(data, headers=headers))

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print("Libro agregado con éxito")

    def eliminar_libro(self, id):
        for libro in self.libros:
            if libro.id == id:
                self.libros.remove(libro)
                print("Libro eliminado con éxito")
                return
        print("No se encontró el libro")

    def buscar_libro(self, filtro):
        headers = ["ID", "Título", "Género", "ISBN", "Editorial", "Autores"]
        data = []
        for libro in self.libros:
            if filtro.lower() in libro.titulo.lower() or filtro in libro.ISBN:
                data.append([libro.id, libro.titulo, libro.genero, libro.ISBN, libro.editorial, "; ".join(libro.autores)])
        print(tabulate(data, headers=headers))

    def ordenar_libros(self):
        self.libros.sort(key=lambda libro: libro.titulo)
        print("Libros ordenados por título")

    def buscar_por_atributo(self, atributo, valor):
        headers = ["ID", "Título", "Género", "ISBN", "Editorial", "Autores"]
        data = []
        for libro in self.libros:
            if getattr(libro, atributo) == valor:
                data.append([libro.id, libro.titulo, libro.genero, libro.ISBN, libro.editorial, "; ".join(libro.autores)])
        print(tabulate(data, headers=headers))

    def buscar_por_numero_autores(self, n):
        headers = ["ID", "Título", "Género", "ISBN", "Editorial", "Autores"]
        data = []
        for libro in self.libros:
            if len(libro.autores) == n:

    def editar_libro(self, id, atributo, valor):
        for libro in self.libros:
            if libro.id == id:
                setattr(libro, atributo, valor)
                print("Libro editado con éxito")
                return
        print("No se encontró el libro")

    def guardar_archivo(self, archivo):
        with open(archivo, "w") as f:
            for libro in self.libros:
                autores = ";".join(libro.autores)
                linea = f"{libro.id},{libro.titulo},{libro.genero},{libro.ISBN},{libro.editorial},{autores}\n"
                f.write(linea)
        print("Libros guardados en archivo")

if __name__ == "__main__":
    biblioteca = Biblioteca()

    while True:
        print("Menú de opciones")
        print("1. Leer archivo")
        print("2. Listar libros")
        print("3. Agregar libro")
        print("4. Eliminar libro")
        print("5. Buscar libro")
        print("6. Ordenar libros")
        print("7. Buscar libros por atributo")
        print("8. Buscar libros por número de autores")
        print("9. Editar libro")
        print("10. Guardar archivo")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            archivo = input("Ingrese el nombre del archivo: ")
            biblioteca.leer_archivo(archivo)
        elif opcion == "2":
            biblioteca.listar_libros()
        elif opcion == "3":
            id = input("Ingrese el ID: ")
            titulo = input("Ingrese el título: ")
            genero = input("Ingrese el género: ")
            ISBN = input("Ingrese el ISBN: ")
            editorial = input("Ingrese la editorial: ")
            autores = input("Ingrese los autores separados por ; : ").split(";")
            libro = Libro(id, titulo, genero, ISBN, editorial, autores)
            biblioteca.agregar_libro(libro)
        elif opcion == "4":
            id = input("Ingrese el ID del libro a eliminar: ")
            biblioteca.eliminar_libro(id)
        elif opcion == "5":
            filtro = input("Ingrese el título o ISBN del libro: ")
            biblioteca.buscar_libro(filtro)
        elif opcion == "6":
            biblioteca.ordenar_libros()
        elif opcion == "7":
            atributo = input("Ingrese el atributo (titulo, genero, ISBN, editorial): ")
            valor = input("Ingrese el valor del atributo: ")
            biblioteca.buscar_por_atributo(atributo, valor)
        elif opcion == "8":
            n = input("Ingrese el número de autores: ")
            biblioteca.buscar_por_numero_autores(int(n))
        elif opcion == "9":
            id = input("Ingrese el ID del libro a editar: ")
            atributo = input("Ingrese el atributo a editar (titulo, genero, ISBN, editorial): ")
            valor = input("Ingrese el valor del atributo: ")
            biblioteca.editar_libro(id, atributo, valor)
        elif opcion == "10":
            archivo = input("Ingrese el nombre del archivo: ")
            biblioteca.guardar_archivo