class Personaje:
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida):
        self.nombre=nombre
        self.fuerza=fuerza
        self.inteligencia=inteligencia
        self.defensa=defensa
        self.vida=vida

    def atributos(self):
        print(self.nombre,":",sep="")
        print("-Fuerza:",self.fuerza)
        print("-Inteligencia:",self.inteligencia)
        print("-Defensa:",self.defensa)
        print("-Vida:",self.vida)
    
    def subir_nivel(self,fuerza,inteligencia,defensa):
        self.fuerza=self.fuerza+fuerza
        self.inteligencia=self.inteligencia+inteligencia
        self.defensa=self.defensa+defensa
    
    def esta_vivo(self):
        return self.vida>0
    
    def morir(self):
        self.vida=0
        print(self.nombre,"ha muerto")
    
    def daño(self,enemigo):
        return self.fuerza - enemigo.defensa

    #esta reutilizando el metodo daño()
    def atacar(self,enemigo):
        daño=self.daño(enemigo)
        enemigo.vida=enemigo.vida-daño
        print(self.nombre,"ha realizado", daño,"puntos de daño a",enemigo.nombre)
        print("La vida de",enemigo.nombre,"es",enemigo.vida)

#creacion de 2 objetos
mi_personaje=Personaje("BitBoss",10,1,5,100)
mi_enemigo=Personaje("Enemy Stando",8,5,3,5)


print(mi_personaje.daño(mi_enemigo))
#mi_personaje.subir_nivel(1,1,1)
#print(mi_personaje.esta_vivo())
#mi_personaje.morir()



