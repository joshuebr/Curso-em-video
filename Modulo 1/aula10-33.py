print('\nDesafio 33 - Identificando qual dos três números,\nsão maiores e menores.')
while True:
    n1 = int(input('\nDigite o primeiro número?:'))
    n2 = int(input('\nDigite o segundo número?:'))
    n3 = int(input('\nDigite o terceiro número?:'))
    maior = n1
    if n2 > n1 and n2 > n3:
        maior = n2
    if n3 > n1 and n3 > n2:
        maior = n3
    menor = n1
    if n2 < n1 and n2 < n3:
        menor = n2
    if n3 < n1 and n3 < n2:
        menor = n3
    print('\nO número {}, é o maior.'
          '\nE o número {}, é o menor.\n\nFIM!!'.format(maior, menor))



