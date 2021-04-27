# Exercício 4 e 5 Baseados em uma página contendo detalhes sobre um livro http://books.toscrape.com/catalogue/the-grand-design_405/index.html , faça a extração dos campos título, preço, descrição e url contendo a imagem de capa do livro.
# O preço deve vir somente valores numéricos e ponto. Ex: Â£13.76 -> 13.76 .
# A descrição de ter o sufixo "more..." removido quando existir.
# # Os campos extraídos devem ser apresentados separados por vírgula. Ex: título,preço,descrição,capa.
from parsel import Selector
import requests

base_url = "http://books.toscrape.com/catalogue/"

response = requests.get(
    f"{base_url}the-grand-design_405/index.html"
)

selector = Selector(text=response.text)

title = selector.css(".product_main h1::text").get()
price = selector.css(".price_color::text").re(r"\d+\.\d{2}")[0]
description = selector.css(".product_page > p::text").get()
url = selector.css('img[alt="The Grand Design"]::attr(src)').get()
in_stock = selector.css(".product_main p").get()
suffix = "...more"
if(description.endswith(suffix)):
    description = description[:-len(suffix)]
print(f"{title}, {price}, {description}, {base_url+url}, {in_stock}")
