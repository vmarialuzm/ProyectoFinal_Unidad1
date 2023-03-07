import csv
    

class Libro:
    def __init__(self,id, titulo, genero, ISBN, editorial, autor):
        self.id=id
        self.titulo=titulo
        self.genero=genero
        self.ISBN=ISBN
        self.editorial=editorial
        self.autor=autor

    def opcion1(self):
        pass

    def opcion2(self):
        print(f"Id: {self.id}")
        print(f"Titulo: {self.titulo}")
        print(f"Genero: {self.genero}")
        print(f"ISBN: {self.ISBN}")
        print(f"Editorial: {self.editorial}")
        print(f"Autor: {self.autor}")

    def opcion5(self):
        input(f"Buscar libro por ISBN o por titulo?  ")
    
    
with open("libros.csv","r") as file:
    reader=csv.DictReader(file)

    for read in reader:
        libro=Libro(read["Id"],read["Titulo"],read["Genero"],read["ISBN"],read["Editorial"],read["Autor"])
        libro.opcion2()
        print("-"*100)  
    