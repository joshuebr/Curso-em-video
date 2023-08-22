import sys

print('\nDesafio 49 - Tabuada II.')

try:
    n = int(input('\nDigite um número para ver sua tabuada:'))

    while(n < 1 ):
        print('\nDigite somente números acima de 1!!!!:', end= ' ')
        n = int(input());
    print('=' * 37)
    for i in range(1, 11 ):
        c = n * i
        print('|| {} X {} = {}'.format(n, i, c))
    print('=' * 37)

except ValueError:
    print('\nVocê digitou valores incorretos!' 
          '\n\n','xX' * 40, 'FIM!!', 'Xx' * 100)
    sys.exit(1)