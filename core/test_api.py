import requests
import json
from core.base_service import BaseService
def test_api_dog():
    url = 'https://dog.ceo/api/breeds/list/all'
    response_1 = requests.request("GET", url)
    body = response_1.json()['message']
    first_dog = list(body.keys())[0]
    print(first_dog)

    url = f"https://dog.ceo/api/breed/{first_dog}/images"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

    assert response.status_code == 200

def test_api_cat():
    url = f"https://api.thecatapi.com/v1/images/search?limit=10"
    response = requests.request("GET", url)
    body = response.json()[0]

    print(body)
    print(response.text)

def test_get_respons():
    response = BaseService.get('https://api.thecatapi.com/v1/images/search?limit=10')
    print(response)
