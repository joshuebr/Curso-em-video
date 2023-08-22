from time import sleep
print('\ndesafio 79 - adicionando valores com opção de continuar e colocando em ordem!'.title())
valores = []

while True:
    n = int(input('\ndigite um valor: '.title()))
    if n not in valores:
        valores.append(n)
        print(f'\nvalor {n} adicionado com sucesso...'.title())
    else:
         print(f'\no valor {n}, já existe e não será adicionado!'.title())

    continuar = str(input('\ndeseja continuar? [S/N]: '.title())).strip().upper()[0]
    while continuar not in 'SsNn':
        continuar = str(input('\ndeseja continuar? [S/N]: '.title())).strip().upper()[0]
    if continuar in 'Nn':
        break
valores.sort()
print('\ncalculando...'.upper())
sleep(0.5)
print()
print(f'\nos valores digitados foram {valores}'.title(), end='')


