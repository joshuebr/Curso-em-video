print('\ndesafio 84 - nome e peso.'.title())
pessoas = []
gordos = []
p = 0
maior = 0
menor = 0
while True:
    gordos.append(str(input('\nNome: ')))
    gordos.append(float(input('\nPeso: ')))
    if len(pessoas) == 0:
        maior = menor = gordos[1]
    else:
        if gordos[1] > maior:
            maior = gordos[1]
        if gordos[1] < menor:
            menor = gordos[1]
    pessoas.append(gordos[:])
    gordos.clear()
    p += 1
    cont = str(input('\nDeseja Continuar?[S/N]: '))
    while cont not in 'SsNn':
        cont = str(input('\nDeseja Continuar?[S/N]: '))
    if cont in 'Nn':
        print('\nCalculando...')
        break
print(f'\nao todo você cadastrou {p} pessoas.'.title())
print()
print(f'\no maior peso foi de {maior}kg, de: '.title(), end='')
for diunas in pessoas:
    if diunas[1] == maior:
     print(f'[{diunas[0]}] '.title(), end='')
print(f'\no menor peso foi de {menor}kg, de: '.title(), end='')
for leves in pessoas:
    if leves[1] == menor:
        print(f'[{leves[0]}] '.title(), end='')