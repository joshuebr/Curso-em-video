from random import randint
from time import sleep
print('\nCriando uma lista de números automáticos e somando os pares, usando funções.')
num = []


def sorteia():
    n = randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5)
    num.append(n)
    print(f'Sorteando os auto valores de 1 a 5:', end='')
    for valor in n:
        print(f'->{valor}', end='')
        sleep(0.70)
    print('...PRONTO!')


def soma():
    for chave, valor in enumerate(num):
        cont = 0
        for dado in valor:
            if dado % 2 == 0:
                cont += dado
        print(f'Somando os pares em {valor}, temos {cont}.', end='')


sorteia()
soma()
print(' FIM!!!')
