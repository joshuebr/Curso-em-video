print('\ndesafio 87 - aprimorando a matriz 3x3.'.title())
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
col = maior = par = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'\ndigite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]

print('@' * 37)
for l in range(0, 3):
    col += matriz[l][2]
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('@' * 37)
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'\na soma dos valores pares é : {par}.'.title())
print(f'\na soma dos valores da terceira coluna é: {col}.'.title())
print(f'\no maior valor da segunda linha é: {maior}.'.title())



