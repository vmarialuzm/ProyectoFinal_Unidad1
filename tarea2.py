import requests
from tabulate import tabulate

url1="https://pokeapi.co/api/v2/generation/"

def listar_generacion(num_generacion):
    
    headers=["Nombre","Habilidad","URL Imagen"]
    response=requests.get(url1+str(num_generacion))
    
    if response.status_code==200:
        response_json=response.json()
        name_pokemon=[ nombre["name"] for nombre in response_json["pokemon_species"]]
        
        url_pokemon="https://pokeapi.co/api/v2/pokemon/"
         
        contador=0
        lista_opciones=[]
        for pokemon in name_pokemon:
            contador+=1
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

url2="https://pokeapi.co/api/v2/pokemon-shape/"

def listar_forma(num_forma):
    
    response=requests.get(url2+str(num_forma))
    
    if response.status_code==200:
        response_json=response.json()
        name_pokemon=[ nombre["name"] for nombre in response_json["pokemon_species"]]

        url_pokemon="https://pokeapi.co/api/v2/pokemon/"

        for pokemon in name_pokemon:
            response=requests.get(url_pokemon+pokemon)
            if response.status_code==200:
                response_json=response.json()

                habilidad_pokemon=[habilidad["ability"]["name"] for habilidad in response_json["abilities"]]
                url_imagen_pokemon=response_json["sprites"]["front_default"]

            print(f"{pokemon},{habilidad_pokemon},{url_imagen_pokemon}")

#-----------------------------------------------------------------------

url3="https://pokeapi.co/api/v2/ability/"

def listar_habilidad(num_habilidad):
    
    response=requests.get(url3+str(num_habilidad))
    
    if response.status_code==200:
        response_json=response.json()

        name_pokemon=[ nombre["pokemon"]["name"] for nombre in response_json["pokemon"]]
        url_pokemon=[ url["pokemon"]["url"] for url in response_json["pokemon"]]

        contador=len(name_pokemon)+1
        for url in url_pokemon:
            contador-=1
            response=requests.get(url)
            if response.status_code==200:
                response_json=response.json()

                habilidad_pokemon=[habilidad["ability"]["name"] for habilidad in response_json["abilities"]]
                url_imagen_pokemon=response_json["sprites"]["front_default"]
        
            print(f"{name_pokemon[len(name_pokemon)-contador]},{habilidad_pokemon},{url_imagen_pokemon}")

#-----------------------------------------------------------------------

url4="https://pokeapi.co/api/v2/pokemon-habitat/"

def listar_habitat(num_habitat):
    
    response=requests.get(url4+str(num_habitat))
    
    if response.status_code==200:
        response_json=response.json()
        name_pokemon=[ nombre["name"] for nombre in response_json["pokemon_species"]]

        url_pokemon="https://pokeapi.co/api/v2/pokemon/"

        for pokemon in name_pokemon:
            response=requests.get(url_pokemon+pokemon)
            if response.status_code==200:
                response_json=response.json()

                habilidad_pokemon=[habilidad["ability"]["name"] for habilidad in response_json["abilities"]]
                url_imagen_pokemon=response_json["sprites"]["front_default"]

            print(f"{pokemon},{habilidad_pokemon},{url_imagen_pokemon}")

#-----------------------------------------------------------------------

url5="https://pokeapi.co/api/v2/type/"       

def listar_tipo(num_tipo):
    
    response=requests.get(url5+str(num_tipo))
    
    if response.status_code==200:
        response_json=response.json()

        name_pokemon=[ nombre["pokemon"]["name"] for nombre in response_json["pokemon"]]
        url_pokemon=[ url["pokemon"]["url"] for url in response_json["pokemon"]]

        contador=len(name_pokemon)+1
        for url in url_pokemon:
            contador-=1
            response=requests.get(url)
            if response.status_code==200:
                response_json=response.json()

                habilidad_pokemon=[habilidad["ability"]["name"] for habilidad in response_json["abilities"]]
                url_imagen_pokemon=response_json["sprites"]["front_default"]
        
            print(f"{name_pokemon[len(name_pokemon)-contador]},{habilidad_pokemon},{url_imagen_pokemon}")
           
#-----------------------------------------------------------------------

def elegir_funciones():
    print(f"El programa puede realizar las siguientes funciones: ")
    lista_opciones=["generación","forma","habilidad","habitat","tipo"]
    for contador,i in enumerate(lista_opciones,start=1):
        print(f"Opción {contador} -> Listar pokemones por {i}")

    funcion_elegida=input(f"Ingrese el número de opción a elegir: ")

    if funcion_elegida=="1":
        elegir_opciones(funcion_elegida)
        opcion_elegida=input(f"Ingrese el número de opción a elegir:")
        listar_generacion(opcion_elegida)
    
    elif funcion_elegida=="2":
        elegir_opciones(funcion_elegida)
        opcion_elegida=input(f"Ingrese el número de opción a elegir:")
        listar_forma(opcion_elegida)

    elif funcion_elegida=="3":
        elegir_opciones(funcion_elegida)
        opcion_elegida=input(f"Ingrese el número de opción a elegir:")
        listar_habilidad(opcion_elegida)
    
    elif funcion_elegida=="4":
        elegir_opciones(funcion_elegida)
        opcion_elegida=input(f"Ingrese el número de opción a elegir:")
        listar_habitat(opcion_elegida)
    
    elif funcion_elegida=="5":
        elegir_opciones(funcion_elegida)
        opcion_elegida=input(f"Ingrese el número de opción a elegir:")
        listar_tipo(opcion_elegida)

    
def elegir_opciones(funcion_elegida):

    lista_url=[url1,url2,url3,url4,url5]

    url=lista_url[int(funcion_elegida)-1]

    response=requests.get(url)
    response_json=response.json()
    opciones_generacion=[i["name"] for i in response_json["results"]]

    for contador,opcion in enumerate(opciones_generacion,start=1):
        print(f"Opcion {contador} -> {opcion}")
            
    


elegir_funciones()