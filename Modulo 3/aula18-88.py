from random import randint
from time import sleep
print('\ndesafio 88 - palpites da mega sena.'.title())
lista = []
listafinal = []
tot = 1
print('@' * 39)
print(f'       palpites sorteados:'.upper())
print('@' * 39)
jogos = int(input('em quantos jogos você quer meu palpite?: '.title()))
print('xX'* 21)
while tot <= jogos:
    cont = 0
    while True:
        d = randint(1, 60)
        if not d in lista:
            lista.append(d)
            lista.sort()
            cont += 1
        if cont >= 6:
            break
    listafinal.append(lista[:])
    lista.clear()
    tot += 1
for x, l in enumerate(listafinal):
    print(f'jogo {x}: {l} '.title())







