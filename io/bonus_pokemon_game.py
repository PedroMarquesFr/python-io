import json
import random


def read_pokemons():
    with open("pokemons.json") as file:
        pokemons = json.load(file)["results"]
    return pokemons


if __name__ == "__main__":
    pokemons = read_pokemons()
    choosen_pokemon = random.choice(pokemons)
    print(choosen_pokemon)
    tip = ""

    for index in range(len(choosen_pokemon["name"])):
        print(tip)
        attempt = input("Qual e esse pokemon??")
        if attempt == choosen_pokemon["name"]:
            print("certa resposta")
            break
        tip += choosen_pokemon["name"][index]