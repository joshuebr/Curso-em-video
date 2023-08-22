print('\nDesafio 52 - Números primos.')
n = int(input('\nDigite um número: '))
calc = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', end='')
        calc += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\n\n\033[mO número {} foi divisível \033[32m{} vezes.'.format(n, calc))