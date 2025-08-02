# A way to connect to an API using python
import requests
base_url = 'https://pokeapi.co/api/v2/'
def get_pokemon_info(name):
    url = f'{base_url}/pokemon/{name}'
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        pokemon_date = response.json()
        return pokemon_date
    else:
        print('failed to retrieve data')
pokemonData = get_pokemon_info('typhlosion')
if pokemonData:
    print(f'name: {pokemonData['name'].capitalize()}')
    print(f'ID: {pokemonData['id']}')
    print(f'hight: {pokemonData['height']}')
    print(f'weight: {pokemonData['weight']}')