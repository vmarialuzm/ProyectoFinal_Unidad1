import csv

class Persona:
    def _init_(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def _repr_(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"

# Lista de personas
personas = [
    Persona("Juan", 30),
    Persona("Maria", 25),
    Persona("Pedro", 40),
]

# Escribir personas en archivo CSV
with open("personas.csv", mode="w", newline="") as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow(["nombre", "edad"]) # escribir cabecera
    for persona in personas:
        writer.writerow([persona.nombre, persona.edad])

# Leer personas del archivo CSV
with open("personas.csv", mode="r") as archivo_csv:
    reader = csv.DictReader(archivo_csv)
    for fila in reader:
        nombre = fila["nombre"]
        edad = int(fila["edad"])
        persona = Persona(nombre, edad)
        print(persona)