# Exercício 2: Jogo da palavra embaralhada. Desenvolva um jogo em que a pessoa usuária tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras e escolherá uma aleatoriamente. O jogador terá três tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se a pessoa ganhou ou perdeu o jogo.
# 🦜 Para embaralhar uma palavra faça: scrambled_word = "".join(random.sample(word, len(word)))
# 🦜 O sorteio de uma palavra aleatória pode ser feito utilizando o método choice: random.choice(["word1", "word2", "word3"]) -> "word2" .
# Exercício 3: Modifique o exercício anterior para que as palavras sejam lidas de um arquivo. Considere que o arquivo terá cada animal em uma linha.

import random

# import json


def retrieve_words(file):
    return [word.strip() for word in file]


def get_word_from_file():
    with open("palavras.txt") as file:
        return retrieve_words(file)


def scramble():
    words = get_word_from_file()
    word = random.choice(words)
    scrambled_word = "".join(random.sample(word, len(word)))
    for i in range(3):
        resp = input("qual e essa palavra: {}:".format(scrambled_word))
        if resp == word:
            print("voce e top")
            break
        else:
            print("resp errada, tentativa {}".format(i + 1))


scramble()
