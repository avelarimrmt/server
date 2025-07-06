import requests
from utils.config import BASE_URL

def post(endpoint: str, json=None, headers=None):
    return requests.post(f"{BASE_URL}{endpoint}", json=json, headers=headers)

def patch(endpoint: str, json=None, headers=None):
    return requests.patch(f"{BASE_URL}{endpoint}", json=json, headers=headers)