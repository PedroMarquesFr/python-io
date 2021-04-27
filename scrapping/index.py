from parsel import Selector
import requests
from pymongo import MongoClient


# response = requests.get("http://books.toscrape.com/")
# selector = Selector(text=response.text)
# # O título está no atributo title em um elemento âncora (<a>)
# # Dentro de um h3 em elementos que possuem classe product_pod
# titles = selector.css(".product_pod h3 a::attr(title)").getall()
# # Estamos utilizando a::attr(title) para capturar somente o valor contido no texto do seletor

# # Os preços estão no texto de uma classe price_color
# # Que se encontra dentro da classe .product_price
# prices = selector.css(".product_price .price_color::text").getall()

# # Combinando tudo podemos buscar os produtos
# # em em seguida buscar os valores individualmente
# for product in selector.css(".product_pod"):
#     title = product.css("h3 a::attr(title)").get()
#     price = product.css(".price_color::text").get()
#     print(title, price)

# print(selector)


# Define a primeira página como próxima a ter seu conteúdo recuperado
URL_BASE = "http://books.toscrape.com/catalogue/"
next_page_url = "page-1.html"
while next_page_url:
    # Busca o conteúdo da próxima página
    response = requests.get(URL_BASE + next_page_url)
    selector = Selector(text=response.text)
    book = {}
    # Imprime os produtos de uma determinada página
    for product in selector.css(".product_pod"):
        title = product.css("h3 a::attr(title)").get()
        price = product.css(".price_color::text").re(r"£\d+\.\d{2}")[0]

        detail_url = product.css("h3 a::attr(href)").get()
        detail_response = requests.get(URL_BASE + detail_url)
        detail_page = Selector(text=detail_response.text)
        description = detail_page.css(".product_page > p::text").get()
        print(title, " - ", description)
        suffix = "...more"
        if description.endswith(suffix) and description is not None:
            description = description[: -len(suffix)]

        book = {"title": title, "price": price, "description": description}

    # Descobre qual é a próxima página
    next_page_url = selector.css(".next a::attr(href)").get()
    with MongoClient() as client:
        db = client.catalogue
        document_id = db.books.insert_one(book).inserted_id
        print(document_id)
