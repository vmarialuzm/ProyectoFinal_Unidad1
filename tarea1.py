import csv
    

class Libro:
    def __init__(self,id,titulo,genero,isbn,editorial,autor):
        self.id=id
        self.titulo=titulo
        self.genero=genero
        self.isbn=isbn
        self.editorial=editorial
        self.autor=autor

    def opcion1(self):
        pass

    def opcion2(self):
        print(f"Id: {self.id}")
        print(f"Titulo: {self.titulo}")
        print(f"Genero: {self.genero}")
        print(f"ISBN: {self.isbn}")
        print(f"Editorial: {self.editorial}")
        print(f"Autor: {self.autor}")


    def opcion5(self,libros,opciones_isbn,opciones_titulo):
        buscar_libro=input(f"Buscar libro por ISBN o por titulo?  ")

        if buscar_libro =="ISBN":
            print(f"Tienes las siguientes opciones: {opciones_isbn}")
            respuesta_ISBN=input(f"Cuál eliges? ")
            
            # Crear una lista temporal para almacenar los libros que coinciden con la búsqueda
            resultados1 = [libro for libro in libros if libro.isbn == respuesta_ISBN]

            print("-"*100) 

            if len(resultados1) == 0:
                print("No se encontraron resultados.")
            else:
                # Iterar sobre la lista de resultados e imprimir los detalles de cada libro
                for libro in resultados1:
                    libro.opcion2()
                   

        elif buscar_libro =="titulo":
            print(f"Tienes las siguientes opciones: {opciones_titulo}")
            respuesta_titulo=input(f"Cuál eliges? ")

            resultados2 = [libro for libro in libros if libro.titulo == respuesta_titulo]

            print("-"*100) 

            if len(resultados2) == 0:
                print("No se encontraron resultados")
            else:
                for libro in resultados2:
                    libro.opcion2()

libros=[]
    
with open("libros.csv","r") as file:
    reader=csv.DictReader(file)


    for read in reader:
        libro=Libro(read["Id"],read["Titulo"],read["Genero"],read["ISBN"],read["Editorial"],read["Autor"])
        #libro.opcion2()
        #print("-"*100) 
        libros.append(libro)

    #lista de opciones metodo opcion5()
    opciones_isbn=[libro.isbn for libro in libros]
    opciones_titulo=[libro.titulo for libro in libros]

    libro.opcion5(libros,opciones_isbn,opciones_titulo)
    
    
    
    

     
    
    