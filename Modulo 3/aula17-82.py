print('\ndesafio 82 - inserindo números e criando 3 listas!'.title())
lista = []
lispar = []
lisimp = []
while True:
    n = int(input('\ndigite um número: '.title()))
    continuar = str(input('\ndeseja continuar? [S/N]: '.title())).strip().upper()[0]
    if n not in lista:
        lista.append(n)
        if n % 2 == 0:
            lispar.append(n)
        else:# n % 3 == 1:
            lisimp.append(n)
    while continuar not in 'SsNn':
        continuar = str(input('\ndeseja continuar? [S/N]: '.title())).strip().upper()[0]
    if continuar in 'Nn':
        break
lista.sort()
lispar.sort()
lisimp.sort()
print('@' * 70)
print()
print(f'\nos numeros que você digitou foram: {lista}'
      f'\na lista de pares é : {lispar}'
      f'\na lista de ímpar é : {lisimp}'.title())
print()
print('@' * 70)

