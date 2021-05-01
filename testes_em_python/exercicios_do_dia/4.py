# Exercício 4 Baseado no exercício anterior, escreva uma função que, dado uma
# lista de emails,
# deve retornar somente os emails válidos. Caso uma exceção ocorra, apenas a
# escreva na tela.
# Exemplo: ["nome@dominio.com", "errad#@dominio.com", "outro@dominio.com"] ->
# ["nome@dominio.com", "outro@dominio.com"]
import re


def if_emails_are_valid(emails: list):
    regex = (
        r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
    )
    valid_emails = []
    for email in emails:
        if re.findall(regex, email):
            valid_emails.append(email)
    return valid_emails


print(
    if_emails_are_valid(
        ["nome@dominio.com", "erraddominio.com", "outro@dominio.com"]
    )
)
