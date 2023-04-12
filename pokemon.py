import requests

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

if __name__ == '__main__':
    dados_pokemon = retorna_dados_pokemon('charizard')
    habilidades = []
    for habilidade in dados_pokemon['abilities']:
        habilidades.append(habilidade['ability']['name'])
    print(habilidades)

