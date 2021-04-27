from pymongo import MongoClient

with MongoClient() as client:
    db = client.catalogue
    # book representa um dado obtido na raspagem
    book = {
        "title": "A Light in the Attic",
    }

    documents = [
        {
            "title": "A Light in the Attic",
        },
        {
            "title": "Tipping the Velvet",
        },
        {
            "title": "Soumission",
        },
    ]

    document_id = db.books.insert_one(book).inserted_id
    db.books.insert_many(documents)
    print(document_id)

    for book in db.books.find({"title": {"$regex": "t"}}):
        print(book["title"])

    client.close()  # fecha a conexão com o banco de dados
