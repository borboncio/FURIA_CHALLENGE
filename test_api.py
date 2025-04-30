import requests

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAACxU0wEAAAAA0tCmEFGM135qL%2FEI8JQSIKZsCTI%3D8switvpFR1puMOxNBPK9VDhEBe2QrI4k3hemTZ0xgkqwu7RTUF'  # Substitua pelo seu token real

headers = {
    'Authorization': f'Bearer {BEARER_TOKEN}',
    'Content-Type': 'application/json',
}

# Exemplo de endpoint para buscar tweets
url = "https://api.twitter.com/2/tweets/search/recent?query=FURIA&max_results=10"


response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Conexão bem-sucedida!")
    print("Tweets encontrados:", response.json())
else:
    print(f"Falha na requisição: {response.status_code}")
    print(response.json())