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

    def opcion1(self):
        pass

    def opcion2(self,libros):
        headers=["Id","Titulo","Genero","ISBN","Editorial","Autor"]
        lista_opciones=[[libro.id,libro.titulo,libro.genero,libro.isbn,libro.editorial,libro.autor] for libro in libros]
        print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))

    def opcion3(self):
        #abriendo el archivo modo append
        with open("libros.csv","a",newline='') as libros_csv:
            # Crear un objeto escritor de CSV
            writer=csv.writer(libros_csv)

            # Pedir al usuario que ingrese los datos del libro
            id=input(f"Id: ")
            titulo=input(f"Titulo: ")
            genero=input(f"Genero: ")
            isbn=input(f"ISBN: ")
            editorial=input(f"Editorial: ")
            autor=input(f"Autor: ")

            #escribir datos en el archivo csv
            writer.writerow([id,titulo,genero,isbn,editorial,autor])
            print("Se agregó el libro exitosamente.")

    def opcion4(self):
        # Abrir el archivo libros.csv en modo lectura y escritura
        with open("libros.csv", "r+") as libros_csv:
            # Leer todas las filas del archivo y almacenarlas en una lista
            filas = libros_csv.readlines()
            
            # Eliminar la última fila de la lista
            filas.pop()

            # Volver al inicio del archivo y escribir todas las filas de la lista en el archivo, sobrescribiendo el archivo original
            libros_csv.seek(0)
            libros_csv.writelines(filas)
            libros_csv.truncate()
            
            print("El último libro ha sido eliminado exitosamente.")


    def opcion5(self,libros,opciones_isbn,opciones_titulo):
        headers=["Id","Titulo","Genero","ISBN","Editorial","Autor"]
        buscar_libro=input(f"Buscar libro por ISBN o por titulo?  ")

        if buscar_libro =="ISBN":
            print(f"Tienes las siguientes opciones: {opciones_isbn}")
            respuesta_ISBN=input(f"Cuál eliges? ")
            
            # Crear una lista temporal para almacenar los libros que coinciden con la búsqueda
            resultados1 = [libro for libro in libros if libro.isbn == respuesta_ISBN]

            if len(resultados1) == 0:
                print("No se encontraron resultados.")
            else:
                # Iterar sobre la lista de resultados e imprimir los detalles de cada libro
                lista_opciones=[[libro.id,libro.titulo,libro.genero,libro.isbn,libro.editorial,libro.autor] for libro in resultados1]
                print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))

                   

        elif buscar_libro =="titulo":
            print(f"Tienes las siguientes opciones: {opciones_titulo}")
            respuesta_titulo=input(f"Cuál eliges? ")

            resultados2 = [libro for libro in libros if libro.titulo == respuesta_titulo]

            if len(resultados2) == 0:
                print("No se encontraron resultados")
            else:
                lista_opciones=[[libro.id,libro.titulo,libro.genero,libro.isbn,libro.editorial,libro.autor] for libro in resultados2]
                print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))

    #metodo para ordenar alfabeticamente por titulo
    def opcion6(self,libros,opciones_titulo):
        headers=["Id","Titulo","Genero","ISBN","Editorial","Autor"]
        lista_desordenada=opciones_titulo
        lista_ordenada=sorted(lista_desordenada)
        lista_objetos=[]
        #recorremos la lista ordenada
        for titulo in lista_ordenada:
            #recorremos la lista de objetos
            for libro in libros:
                #aplicamos el metodo opcion2() segun el orden de la lista ordenada
                if titulo==libro.titulo:
                    lista_objetos.append(libro)

        lista_opciones=[[libro.id,libro.titulo,libro.genero,libro.isbn,libro.editorial,libro.autor] for libro in lista_objetos]
        print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))
        

    def opcion7(self,libros,opciones_autor,opciones_editorial,opciones_genero):
        headers=["Id","Titulo","Genero","ISBN","Editorial","Autor"]
        buscar_libro=input(f"Buscar libro por autor,editorial o genero?  ")

        if buscar_libro=="autor":
            print(f"Tienes las siguientes opciones: {opciones_autor}")
            respuesta_autor=input(f"Cuál eliges? ")

            resultados_autor=[libro for libro in libros if libro.autor==respuesta_autor]        
            print("-"*100) 
            if len(resultados_autor)==0:
                print("No se encontraron resultados")
            else:
                lista_opciones=[[libro.id,libro.titulo,libro.genero,libro.isbn,libro.editorial,libro.autor] for libro in resultados_autor]
                print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))
        
        elif buscar_libro=="editorial":
            print(f"Tienes las siguientes opciones: {opciones_editorial}")
            respuesta_editorial=input(f"Cuál eliges? ")

            resultados_editorial=[libro for libro in libros if libro.editorial==respuesta_editorial]        
            print("-"*100) 
            if len(resultados_editorial)==0:
                print("No se encontraron resultados")
            else:
                lista_opciones=[[libro.id,libro.titulo,libro.genero,libro.isbn,libro.editorial,libro.autor] for libro in resultados_editorial]
                print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))

        elif buscar_libro=="genero":
            print(f"Tienes las siguientes opciones: {opciones_genero}")
            respuesta_genero=input(f"Cuál eliges? ")

            resultados_genero=[libro for libro in libros if libro.genero==respuesta_genero]        
            print("-"*100) 
            if len(resultados_genero)==0:
                print("No se encontraron resultados")
            else:
                lista_opciones=[[libro.id,libro.titulo,libro.genero,libro.isbn,libro.editorial,libro.autor] for libro in resultados_genero]
                print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))

    def opcion8(self,libros):
        headers=["Id","Titulo","Genero","ISBN","Editorial","Autor"]
        num_autores=int(input("Ingresar número de autores: "))

        libros_encontrados=[]
        #recorrer la lista de objetos
        for libro in libros:
            #si la suma de comas + 1 de cada autor coincide con lo ingresado, lo agregamos a la lista temporal
            if libro.autor.count(" , ")+1 == num_autores:
                libros_encontrados.append(libro)
        
        lista_opciones=[[libro.id,libro.titulo,libro.genero,libro.isbn,libro.editorial,libro.autor] for libro in libros_encontrados]
        print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))
                   
    def opcion9(self,libros,opciones_id):
        edita_libro=int(input(f"Qué libro desea editar? {opciones_id} : "))

        #abrir el archivo csv para lectura
        with open("libros.csv","r") as libros_csv:
            # leer los datos del archivo csv en una lista
            data=list(csv.reader(libros_csv))

            # modificar los siguientes datos
            data[edita_libro][0]=input(f"Id: ")
            data[edita_libro][1]=input(f"Titulo: ")
            data[edita_libro][2]=input(f"Genero: ")
            data[edita_libro][3]=input(f"ISBN: ")
            data[edita_libro][4]=input(f"Editorial: ")
            data[edita_libro][5]=input(f"Autor: ")

            #abrir el archivo csv para escritura
            with open("libros.csv","w",newline="") as file:
                #escribir los datos modificados ne el archivo csv
                writer=csv.writer(file)
                writer.writerows(data)
            print("Se editó el libro exitosamente.")





libros=[]
    
with open("libros.csv","r") as file:
    reader=csv.DictReader(file)


    for read in reader:
        libro=Libro(read["Id"],read["Titulo"],read["Genero"],read["ISBN"],read["Editorial"],read["Autor"])
        libros.append(libro)
    #libro.opcion2(libros)
        
    #lista de opciones metodo opcion5()
    opciones_isbn=[libro.isbn for libro in libros]
    opciones_titulo=[libro.titulo for libro in libros]

    #lista de opciones metodo opcion7()
    opciones_autor=[libro.autor for libro in libros]
    opciones_editorial=[libro.editorial for libro in libros]
    opciones_genero=[libro.genero for libro in libros]

    #lista de opciones metodo opcion9()
    opciones_id=[libro.id for libro in libros]

    #libro.opcion5(libros,opciones_isbn,opciones_titulo)

    #libro.opcion6(libros,opciones_titulo)
    #libro.opcion3()   
    #libro.opcion4()
    #libro.opcion7(libros,opciones_autor,opciones_editorial,opciones_genero)
    libro.opcion8(libros)
    #libro.opcion9(libros,opciones_id)
    
    

     
    
    