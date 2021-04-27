# Exercício 6 Escreva um programa que se conecte ao banco de dados library e liste os livros da coleção books para uma determinada categoria recebida por uma pessoa usuária. Somente o título dos livros deve ser exibido.

from pymongo import MongoClient


# category = input("Escolha uma categoria: ")
with MongoClient() as client:
    db = client.catalogue
    # books = db.booksEx.find({"categories": category}, {"title": 1})
    # for book in books:
    #     print(book)
    num_categories = db.booksEx.aggregate(
        [
            {"$match": {"status": "PUBLISH"}},
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
        ]
    )
    for category in num_categories:
        print(f'{category["_id"]}, {category["count"]}')
