print('\ndesafio 86 - Criando uma matriz de dimensões 3x3.'.title())
lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'\ndigite um valor para [{l}, {c}]: '.title()))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista [l][c]:^5}]', end='')
    print()


