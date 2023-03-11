import requests
from tabulate import tabulate

url1="https://pokeapi.co/api/v2/generation/"

def listar_generacion(num_generacion):
    
    headers=["Nombre","Habilidad","URL Imagen"]
    response=requests.get(url1+str(num_generacion))
    
    if response.status_code==200:
        response_json=response.json()
        #creamos la lista con todos los pokemones de esa generacion
        name_pokemon=[ nombre["name"] for nombre in response_json["pokemon_species"]]
        
        #en este endpoint podemos encontrar la habilidad y URL Imagen
        url_pokemon="https://pokeapi.co/api/v2/pokemon/"
         
        lista_opciones=[]
        for contador,pokemon in enumerate(name_pokemon,start=1):
            #queremos que nos muestre solo los 10 primeros registros
            if contador<11:
                response=requests.get(url_pokemon+pokemon)
                if response.status_code==200:
                    response_json=response.json()

                    habilidad_pokemon=[habilidad["ability"]["name"] for habilidad in response_json["abilities"]]
                    url_imagen_pokemon=response_json["sprites"]["front_default"]
                    
                    #completamos la lista_opciones con los tres datos que nos piden
                    lista_opciones.append([pokemon,habilidad_pokemon,url_imagen_pokemon])
                
            else:
                #utilizamos la libreria tabulate para mostrar en un formato tipo tabla
                print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))
                break          
 
#-----------------------------------------------------------------------

url2="https://pokeapi.co/api/v2/pokemon-shape/"

def listar_forma(num_forma):
    
    headers=["Nombre","Habilidad","URL Imagen"]
    response=requests.get(url2+str(num_forma))
    
    if response.status_code==200:
        response_json=response.json()
        name_pokemon=[ nombre["name"] for nombre in response_json["pokemon_species"]]

        url_pokemon="https://pokeapi.co/api/v2/pokemon/"

        lista_opciones=[]
        for contador,pokemon in enumerate(name_pokemon,start=1):
            if contador<11:
                response=requests.get(url_pokemon+pokemon)
                if response.status_code==200:
                    response_json=response.json()

                    habilidad_pokemon=[habilidad["ability"]["name"] for habilidad in response_json["abilities"]]
                    url_imagen_pokemon=response_json["sprites"]["front_default"]

                    lista_opciones.append([pokemon,habilidad_pokemon,url_imagen_pokemon])
            else:
                print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))
                break

#-----------------------------------------------------------------------

url3="https://pokeapi.co/api/v2/ability/"

#no le coloque la condicional para limitarlo a 10 registros, ya que al elegir pokemones por habilidad son pocos
def listar_habilidad(num_habilidad):
    
    headers=["Nombre","Habilidad","URL Imagen"]
    response=requests.get(url3+str(num_habilidad))
    
    if response.status_code==200:
        response_json=response.json()

        name_pokemon=[ nombre["pokemon"]["name"] for nombre in response_json["pokemon"]]
        url_pokemon=[ url["pokemon"]["url"] for url in response_json["pokemon"]]

        contador=len(name_pokemon)+1
        lista_opciones=[]
        for url in url_pokemon:
            contador-=1
            response=requests.get(url)
            if response.status_code==200:
                response_json=response.json()

                habilidad_pokemon=[habilidad["ability"]["name"] for habilidad in response_json["abilities"]]
                url_imagen_pokemon=response_json["sprites"]["front_default"]
            
                lista_opciones.append([name_pokemon[len(name_pokemon)-contador],habilidad_pokemon,url_imagen_pokemon])
                
        print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))   
     
#-----------------------------------------------------------------------

url4="https://pokeapi.co/api/v2/pokemon-habitat/"

def listar_habitat(num_habitat):
    
    headers=["Nombre","Habilidad","URL Imagen"]
    response=requests.get(url4+str(num_habitat))
    
    if response.status_code==200:
        response_json=response.json()
        name_pokemon=[ nombre["name"] for nombre in response_json["pokemon_species"]]

        url_pokemon="https://pokeapi.co/api/v2/pokemon/"

        lista_opciones=[]
        for contador,pokemon in enumerate(name_pokemon,start=1):
            if contador<11:
                response=requests.get(url_pokemon+pokemon)
                if response.status_code==200:
                    response_json=response.json()

                    habilidad_pokemon=[habilidad["ability"]["name"] for habilidad in response_json["abilities"]]
                    url_imagen_pokemon=response_json["sprites"]["front_default"]

                    lista_opciones.append([pokemon,habilidad_pokemon,url_imagen_pokemon])

            else:
                print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))
                break
            
#-----------------------------------------------------------------------

url5="https://pokeapi.co/api/v2/type/"       

def listar_tipo(num_tipo):
    
    headers=["Nombre","Habilidad","URL Imagen"]
    response=requests.get(url5+str(num_tipo))
    
    if response.status_code==200:
        response_json=response.json()

        name_pokemon=[ nombre["pokemon"]["name"] for nombre in response_json["pokemon"]]
        url_pokemon=[ url["pokemon"]["url"] for url in response_json["pokemon"]]

        contador=len(name_pokemon)+1
        lista_opciones=[]
        for url in url_pokemon:
            contador-=1
            response=requests.get(url)
            if response.status_code==200:
                response_json=response.json()

                habilidad_pokemon=[habilidad["ability"]["name"] for habilidad in response_json["abilities"]]
                url_imagen_pokemon=response_json["sprites"]["front_default"]
        
                lista_opciones.append([name_pokemon[len(name_pokemon)-contador],habilidad_pokemon,url_imagen_pokemon])
                
        print(tabulate(lista_opciones,headers=headers, tablefmt="grid"))   

#-----------------------------------------------------------------------

def listar_funciones():
    #describe y muestra lo que hace cada función
    print(f"El programa puede realizar las siguientes funciones: ")
    lista_opciones=["generación","forma","habilidad","habitat","tipo"]
    for contador,i in enumerate(lista_opciones,start=1):
        print(f"Opción {contador} -> Listar pokemones por {i}")

    #el usuario elige la función que desea
    funcion_elegida=input(f"Ingrese el número de opción a elegir: ")

    #condicional con cada función
    if funcion_elegida=="1":
        listar_opciones(funcion_elegida)
        opcion_elegida=input(f"Ingrese el número de opción a elegir:")
        listar_generacion(opcion_elegida)
    
    elif funcion_elegida=="2":
        listar_opciones(funcion_elegida)
        opcion_elegida=input(f"Ingrese el número de opción a elegir:")
        listar_forma(opcion_elegida)

    elif funcion_elegida=="3":
        listar_opciones(funcion_elegida)
        opcion_elegida=input(f"Ingrese el número de opción a elegir:")
        listar_habilidad(opcion_elegida)
    
    elif funcion_elegida=="4":
        listar_opciones(funcion_elegida)
        opcion_elegida=input(f"Ingrese el número de opción a elegir:")
        listar_habitat(opcion_elegida)
    
    elif funcion_elegida=="5":
        listar_opciones(funcion_elegida)
        opcion_elegida=input(f"Ingrese el número de opción a elegir:")
        listar_tipo(opcion_elegida)

#-----------------------------------------------------------------------
   
def listar_opciones(funcion_elegida):

    lista_url=[url1,url2,url3,url4,url5]

    #se utiliza el parametro funcion_elegida, ya que la funcion 1 trabaja con el url1 y así sucesivamente...
    url=lista_url[int(funcion_elegida)-1]

    response=requests.get(url)
    response_json=response.json()
    opciones_generacion=[i["name"] for i in response_json["results"]]

    #se lista a todas las ociones que se encontró en esa url
    for contador,opcion in enumerate(opciones_generacion,start=1):
        print(f"Opcion {contador} -> {opcion}")

#-----------------------------------------------------------------------

#función para verificar si el usuario quiere seguir haciendo consultas
def volver_consultar():
    while True:
        print("*****BIENVENIDO*****")
        listar_funciones()
        jugar=input(f"Deseas volver a jugar? S/N: ")
        if jugar=="S":
            pass
        else:
            print("Gracias por jugar!!!")
            break

volver_consultar()


            
    


