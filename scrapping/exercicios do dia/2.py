# Exercício 2 Faça uma requisição ao recurso usuários da API do Github
#  ( https://api.github.com/users ), exibindo o username e url de todos
# os usuários retornados.

import requests

response = requests.get("https://api.github.com/users")

arr_of_obj = response.json()

users_obj = {}

for obj in arr_of_obj:
    print(obj["login"], obj["url"])
    users_obj[obj["login"]] = obj["url"]

print(users_obj)
