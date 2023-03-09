import requests

url1="https://pokeapi.co/api/v2/generation/"

def listar_generacion(num_generacion):
    """ response=requests.get(url1)
    response_json=response.json()
    opciones_generacion=[generacion["name"] for generacion in response_json["results"]]

    for contador,opcion in enumerate(opciones_generacion,start=1):
        print(f"Opcion {contador} -> {opcion}")
        
    num_generacion=input(f"Ingrese el número de opción a elegir: ") """


    response=requests.get(url1+num_generacion)
    
    if response.status_code==200:
        response_json=response.json()
        name_pokemon=[ nombre["name"] for nombre in response_json["pokemon_species"]]
        """ habilidad_pokemon=
        url_imagen_pokemon= """
    print(name_pokemon)

#-----------------------------------------------------------------------

url2="https://pokeapi.co/api/v2/pokemon-shape/"


def listar_forma(num_forma):
    response=requests.get(url2+num_forma)
    
    if response.status_code==200:
        response_json=response.json()
        name_pokemon=[ nombre["name"] for nombre in response_json["pokemon_species"]]
        """ habilidad_pokemon=
        url_imagen_pokemon= """
    print(name_pokemon)

#-----------------------------------------------------------------------

url3="https://pokeapi.co/api/v2/ability/"

def listar_habilidad(num_habilidad):
    response=requests.get(url3+num_habilidad)
    
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
    response=requests.get(url4+num_habitat)
    
    if response.status_code==200:
        response_json=response.json()
        name_pokemon=[ nombre["name"] for nombre in response_json["pokemon_species"]]
        """ habilidad_pokemon=
        url_imagen_pokemon= """
    print(name_pokemon)

#-----------------------------------------------------------------------
          
url5="https://pokeapi.co/api/v2/type/"

def listar_tipo(num_tipo):
    response=requests.get(url5+num_tipo)
    
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
           


#listar_generacion("1")
#listar_forma("1")
#listar_habilidad("1")
#listar_tipo("5")

def elegir_opciones():

    response=requests.get(url4)
    response_json=response.json()
    opciones_generacion=[i["name"] for i in response_json["results"]]

    for contador,opcion in enumerate(opciones_generacion,start=1):
        print(f"Opcion {contador} -> {opcion}")
        
    opcion_elegida=input(f"Ingrese el número de opción a elegir: ")
    #listar_generacion(opcion_elegida)
    #listar_forma(opcion_elegida)
    #listar_habilidad(opcion_elegida)
    listar_habitat(opcion_elegida)
    #listar_tipo(opcion_elegida)

elegir_opciones()
