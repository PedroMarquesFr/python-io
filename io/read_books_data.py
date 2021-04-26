import json

def read_data ():
    with open("books.json") as file:
        content = file.read()  # leitura do arquivo
        books = json.loads(content)  # o conteúdo é transformado em
        return books
    # estrutura python equivalente, dicionário neste caso.
    # acessamos a chave results que é onde contém nossa lista de pokemons

read_data()
