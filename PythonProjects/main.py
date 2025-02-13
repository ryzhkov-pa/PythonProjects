import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8220dcda592bc6d4ec1559d150b82c80'
HEADER = {'Content-Type': 'application/json'}
pokemon_id = '233721'

body_creature = {
    "name": "Бульбазавр",
    "photo_id": 1
}
TRAINER_TOKEN = {'trainer_token':TOKEN, 'Content-Type': 'application/json'}
body_pokebol = {
    "pokemon_id": pokemon_id
}
body_put = {
    "pokemon_id": pokemon_id,
    "name": "Python",
    "photo_id": 2
}


response = requests.post(url= f'{URL}/pokemons',headers = TRAINER_TOKEN,  json = body_creature)
print(response.text)



responseput = requests.put(url = f'{URL}/pokemons', headers = TRAINER_TOKEN, json = body_put)
print(responseput.text)


response_pokebal = requests.post(url = f'{URL}/trainers/add_pokeball', headers = TRAINER_TOKEN, json = body_pokebol)
print(responseput.status_code)



