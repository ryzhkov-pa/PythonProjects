import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8220dcda592bc6d4ec1559d150b82c80'
HEADER = {'Content-Type': 'application/json'}
TRAINER_TOKEN = {'trainer_token':TOKEN, 'Content-Type': 'application/json' }
TRAINER_ID = '17672'




def test_status_code():
    responce = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert responce.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get.json ()["data"][0]['trainer_name'] =='LegenDa'
