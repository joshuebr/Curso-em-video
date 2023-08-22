print('\ndesafio 81 - inserindo valores e mostrando algo!'.title())
lista = []
cont = 0
while True:
    n = int(input('\ndigite um valor: '.title()))
    cont += 1
    continuar = str(input('\ndeseja continuar? [S/N]: '.title())).strip().upper()[0]
    if n not in lista:
        lista.append(n)
    while continuar not in 'SsNn':
        continuar = str(input('\ndeseja continuar? [S/N]: '.title())).strip().upper()[0]
    if continuar in 'Nn':
        break
lista.sort(reverse=True)
print('@' * 70)
print(f'\nvocê digitou {cont} valores.'.title())
print()
print('@' * 70)
print(f'\nos valores digitados de forma decrescente foram: {lista}'.title())
print()
print('@' * 70)
if 5 in lista:
    print('\no valor 5 foi digitado e está na lista.'.title())
else:
    print('\no valor 5 não foi digitado e não está na lista.'.title())
print()
print('@' * 70)
