import requests

# requests.get # select, le dados do api publico
# requests.post # insert
# requests.put # update
# requests.delete # delete


response = requests.get('https://www.mercafacil.com.br')
print(response.status_code)

url = 'https://pokeapi.co/api/v2/pokemon/pikachu'
response = requests.get(url)
data = response.json()
print(data)