# Exercício 1: Escreva um programa que retorne uma
#  lista com os valores numéricos de 1 a N, mas com as seguintes exceções :


def fizz_buzz(n):
    fizz_buzz_list = []
    for i in range(1, n):
        print("ue")
        if i % 5 == 0 and i % 3 == 0:
            fizz_buzz_list.append("FizzBuzz")
        elif i % 3 == 0:
            fizz_buzz_list.append("Fizz")
        elif i % 5 == 0:
            fizz_buzz_list.append("Buzz")
        else:
            fizz_buzz_list.append(i)
    return fizz_buzz_list


print(fizz_buzz(100))
