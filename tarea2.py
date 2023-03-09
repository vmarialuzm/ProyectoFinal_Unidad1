import requests

url1="https://pokeapi.co/api/v2/generation/"

def listar_generacion(num_generacion):
    response=requests.get(url1+str(num_generacion))
    
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

def elegir_opciones():
    print(f"El programa puede realizar las siguientes funciones: ")
    print(f"Opción 1 -> Listar pokemones por generación")
    print(f"Opción 2 -> Listar pokemones por forma")
    print(f"Opción 3 -> Listar pokemones por habilidad")
    print(f"Opción 4 -> Listar pokemones por habitat")
    print(f"Opción 5 -> Listar pokemones por tipo")

    url_elegida=int(input(f"Ingrese el número de opción a elegir:"))-1
    lista_url=[url1,url2,url3,url4,url5]

    response=requests.get(lista_url[url_elegida])
    response_json=response.json()
    opciones_generacion=[i["name"] for i in response_json["results"]]

    for contador,opcion in enumerate(opciones_generacion,start=1):
        print(f"Opcion {contador} -> {opcion}")
            
    opcion_elegida=input(f"Ingrese el número de opción a elegir: ")

    lista_funciones=[listar_generacion(opcion_elegida),listar_forma(opcion_elegida),listar_habilidad(opcion_elegida),listar_habitat(opcion_elegida),listar_tipo(opcion_elegida)]
    return lista_funciones[lista_funciones[url_elegida]]

elegir_opciones()
