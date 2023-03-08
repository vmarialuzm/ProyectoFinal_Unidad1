import requests

url="https://pokeapi.co/api/v2/generation/"

def listar_generacion(num_generacion):
    response=requests.get(url+num_generacion)
    
    if response.status_code==200:
        response_json=response.json()
        name_pokemon=[ nombre["name"] for nombre in response_json["pokemon_species"]]
        """ habilidad_pokemon=
        url_imagen_pokemon= """
    print(name_pokemon)

def listar_forma()

listar_generacion("1")
