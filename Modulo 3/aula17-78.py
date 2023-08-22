print('\ndesafio 78 - inserindo 5 valores em uma lista e mostrando maior e menor.'.title())
valores = []
for c in range(1, 6):
    valores.append(int(input(f'digite um valor na posição {c}: '.title())))
print(f'\nvocê digitou os valores: {valores}'.title())
print()
print(f'\no maior valor digitado foi {max(valores)}, nas posições: '.title(), end='')
for v, x in enumerate(valores):
    if x == max(valores):
        print(f'{v+1} <- ', end='')
print()
print(f'\no menor valor digitado foi {min(valores)}, nas posições:  '.title(), end='')
for v, x in enumerate(valores):
    if x == min(valores):
        print(f'{v+1} <- ', end='')
print()
