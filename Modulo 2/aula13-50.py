import sys
print('\nDesafio 50 - Somando números pares, encontrados em 6 valores.')
try:
    soma = 0
    for i in range(1, 7):
        n = int(input('Digite o {}º número inteiro:'.format(i)))
        while(n < 1 or n == 0):
             print('\nDigite valores inteiros!!:', end=' ')
             n = int(input());
        if n % 2 == 0:
            soma += n

    print('\n', 'O resultado dos números pares encontrados e somados são {}.'.format(soma),
         '\n\n', 'xX' * 40, 'FIM!!', 'Xx' * 100)
except ValueError:
    print('\nValores inválidos!!',
          '\n\n', 'xX' * 40, 'FIM!!', 'Xx' * 100)
    sys.exit(1)