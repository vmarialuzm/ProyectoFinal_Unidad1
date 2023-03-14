import csv
from tabulate import tabulate

class Libro:
    def __init__(self,id,titulo,genero,isbn,editorial,autor):
        self.id=id
        self.titulo=titulo
        self.genero=genero
        self.isbn=isbn
        self.editorial=editorial
        self.autor=autor

#-----------------------------------------------------------------------

#se creo 2 clases para más orden 
class Biblioteca:
    #self.libros sera una lista de "n" objetos, porque "n" es la cantidad de registros que tenemos en el archivo csv.
    def __init__(self):
        self.libros=[]

#-----------------------------------------------------------------------

    #agregar un parametro con el nombre del archivo csv
    def leer_archivo(self):
        #libros=[] #lista de objetos(5)
        
        with open("libros.csv","r") as file:
            reader=csv.DictReader(file)  #convertimos al archivo en tipo diccionario
           
            for read in reader:
                #creamos 1 objeto por cada iteración
                libro=Libro(read["Id"],read["Titulo"],read["Genero"],read["ISBN"],read["Editorial"],read["Autor"])
                #agregamos el objeto a la lista vacia que esta en el constructor
                self.libros.append(libro)
       
#-----------------------------------------------------------------------

    def listar_libros(self):
        headers=["Id","Titulo","Genero","ISBN","Editorial","Autor"]
        #usando comprehension
        lista_opciones=[[libro.id,libro.titulo,libro.genero,libro.isbn,libro.editorial,libro.autor] for libro in self.libros]
        print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))

#-----------------------------------------------------------------------

    def agregar_libro(self):
        id=input(f"Id: ")
        titulo=input(f"Titulo: ")
        genero=input(f"Genero: ")
        isbn=input(f"ISBN: ")
        editorial=input(f"Editorial: ")
        autor=input(f"Autor: ")
        #se creo un nuevo objeto
        libro=Libro(id,titulo,genero,isbn,editorial,autor)
        #se agregó a la lista de objetos
        self.libros.append(libro)
        print("Se agregó el libro exitosamente.")

#-----------------------------------------------------------------------

    def eliminar_libro(self):
        print(f"¿Qué libro desea eliminar?")
        self.listar_libros()
        indice_libro=int(input("Ingrese el número de libro que desea eliminar: "))-1
        self.libros.pop(indice_libro)
        print("Se eliminó el libro exitosamente")

#-----------------------------------------------------------------------

    def buscar_isbn_titulo(self):
        headers=["Id","Titulo","Genero","ISBN","Editorial","Autor"]
        buscar_libro=input(f"Buscar libro por ISBN o por titulo?  ")

        opciones_isbn=[libro.isbn for libro in self.libros]
        opciones_titulo=[libro.titulo for libro in self.libros]
        if buscar_libro =="ISBN":
            print(f"Tienes las siguientes opciones: {opciones_isbn}")
            respuesta_ISBN=input(f"Cuál eliges? ")
            
            # Crear una lista temporal para almacenar los libros que coinciden con la búsqueda
            resultados_isbn = [libro for libro in self.libros if libro.isbn == respuesta_ISBN]

            if len(resultados_isbn) == 0:
                print("No se encontraron resultados.")
            else:
                # Iterar sobre la lista de resultados e imprimir los detalles de cada libro
                lista_opciones=[[libro.id,libro.titulo,libro.genero,libro.isbn,libro.editorial,libro.autor] for libro in resultados_isbn]
                print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))

                   

        elif buscar_libro =="titulo":
            print(f"Tienes las siguientes opciones: {opciones_titulo}")
            respuesta_titulo=input(f"Cuál eliges? ")

            resultados_titulo = [libro for libro in self.libros if libro.titulo == respuesta_titulo]

            if len(resultados_titulo) == 0:
                print("No se encontraron resultados")
            else:
                lista_opciones=[[libro.id,libro.titulo,libro.genero,libro.isbn,libro.editorial,libro.autor] for libro in resultados_titulo]
                print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))

#-----------------------------------------------------------------------

    def ordenar_libros(self):
        headers=["Id","Titulo","Genero","ISBN","Editorial","Autor"]
        opciones_titulo=[libro.titulo for libro in self.libros]
        
        lista_desordenada=opciones_titulo
        lista_ordenada=sorted(lista_desordenada)

        lista_objetos=[]

        #recorremos la lista ordenada
        for titulo in lista_ordenada:
            #recorremos la lista de objetos
            for libro in self.libros:
                if titulo==libro.titulo:
                    lista_objetos.append(libro)

        lista_opciones=[[libro.id,libro.titulo,libro.genero,libro.isbn,libro.editorial,libro.autor] for libro in lista_objetos]
        print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))
        
#-----------------------------------------------------------------------

    def buscar_autor_editorial_genero(self):
        headers=["Id","Titulo","Genero","ISBN","Editorial","Autor"]
        buscar_libro=input(f"Buscar libro por autor,editorial o genero?  ")

        opciones_autor=[libro.autor for libro in self.libros]
        opciones_editorial=[libro.editorial for libro in self.libros]
        opciones_genero=[libro.genero for libro in self.libros]

        if buscar_libro=="autor":
            print(f"Tienes las siguientes opciones: {opciones_autor}")
            respuesta_autor=input(f"Cuál eliges? ")

            resultados_autor=[libro for libro in self.libros if libro.autor==respuesta_autor]        
            print("-"*100) 
            if len(resultados_autor)==0:
                print("No se encontraron resultados")
            else:
                lista_opciones=[[libro.id,libro.titulo,libro.genero,libro.isbn,libro.editorial,libro.autor] for libro in resultados_autor]
                print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))
        
        elif buscar_libro=="editorial":
            print(f"Tienes las siguientes opciones: {opciones_editorial}")
            respuesta_editorial=input(f"Cuál eliges? ")

            resultados_editorial=[libro for libro in self.libros if libro.editorial==respuesta_editorial]        
            print("-"*100) 
            if len(resultados_editorial)==0:
                print("No se encontraron resultados")
            else:
                lista_opciones=[[libro.id,libro.titulo,libro.genero,libro.isbn,libro.editorial,libro.autor] for libro in resultados_editorial]
                print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))

        elif buscar_libro=="genero":
            print(f"Tienes las siguientes opciones: {opciones_genero}")
            respuesta_genero=input(f"Cuál eliges? ")

            resultados_genero=[libro for libro in self.libros if libro.genero==respuesta_genero]        
            print("-"*100) 
            if len(resultados_genero)==0:
                print("No se encontraron resultados")
            else:
                lista_opciones=[[libro.id,libro.titulo,libro.genero,libro.isbn,libro.editorial,libro.autor] for libro in resultados_genero]
                print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))

#-----------------------------------------------------------------------

    def buscar_num_autores(self):
        headers=["Id","Titulo","Genero","ISBN","Editorial","Autor"]
        num_autores=int(input("Ingresar número de autores: "))

        libros_encontrados=[]
        #recorrer la lista de objetos
        for libro in self.libros:
            #si la suma de comas + 1 de cada autor coincide con lo ingresado, lo agregamos a la lista temporal
            if libro.autor.count(" , ")+1 == num_autores:
                libros_encontrados.append(libro)
        
        lista_opciones=[[libro.id,libro.titulo,libro.genero,libro.isbn,libro.editorial,libro.autor] for libro in libros_encontrados]
        print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))

#-----------------------------------------------------------------------
                   
    def editar_libros(self):
        print(f"¿Qué libro desea editar?")
        #listamos todos los libros
        self.listar_libros()
        indice_libro=int(input("Ingrese el número de libro que desea editar: "))-1
        id=input(f"Id: ")
        titulo=input(f"Titulo: ")
        genero=input(f"Genero: ")
        isbn=input(f"ISBN: ")
        editorial=input(f"Editorial: ")
        autor=input(f"Autor: ")
        #creamos un objeto
        libro=Libro(id,titulo,genero,isbn,editorial,autor)
        #reeemplamos el objeto con el indice elegido con los datos nuevos
        self.libros[indice_libro]=libro
        print("Se editó el libro exitosamente")

#-----------------------------------------------------------------------

    def guardar_libros(self):
        with open("libros.csv","w", newline='') as f:
            writer=csv.writer(f)
            #escribir la cabecera
            writer.writerow(["Id","Titulo","Genero","ISBN","Editorial","Autor"])
            for libro in self.libros:
                writer.writerow([libro.id,libro.titulo,libro.genero,libro.isbn,libro.editorial,libro.autor])
            print("Se agregó el libro exitosamente.") 

#-----------------------------------------------------------------------

def menu():
    #creamos el objeto
    biblioteca=Biblioteca()

    while True:
        print("Menú de opciones: ")
        print("1. Leer archivo")
        print("2. Listar libros")
        print("3. Agregar libro")
        print("4. Eliminar libro")
        print("5. Buscar libro por ISBN o por título")
        print("6. Ordenar libros por título")
        print("7. Buscar libros por autor, editorial o género")
        print("8. Buscar libros por número de autores")
        print("9. Editar o actualizar datos de un libro")
        print("10. Guardar libros")
        print("0. Salir")

        opcion_elegida=input("Ingrese el número de opción a elegir: ")

        if opcion_elegida=="1":
            print("Archivo cargado exitosamente")
            biblioteca.leer_archivo()
        
        elif opcion_elegida=="2":
            print("Listado de libros: ")
            biblioteca.listar_libros()
        
        elif opcion_elegida=="3":
            biblioteca.agregar_libro()

        elif opcion_elegida=="4":
            biblioteca.eliminar_libro()

        elif opcion_elegida=="5":
            biblioteca.buscar_isbn_titulo()
        
        elif opcion_elegida=="6":
            biblioteca.ordenar_libros()

        elif opcion_elegida=="7":
            biblioteca.buscar_autor_editorial_genero()
        
        elif opcion_elegida=="8":
            biblioteca.buscar_num_autores()
        
        elif opcion_elegida=="9":
            biblioteca.editar_libros()
        
        elif opcion_elegida=="10":
            biblioteca.guardar_libros()
        
        elif opcion_elegida=="0":
            break




#aseguras que el menú interactivo sólo se ejecute si el archivo está siendo ejecutado como programa principal
if __name__ == '__main__':
    menu()

     
    
    