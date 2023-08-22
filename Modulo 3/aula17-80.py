print('\ndesafio 80 - inserindo valores em suas respectivas posições!'.title())
valores = []

for c in range(0, 5):
    print()
    n = int(input('\ndigite um valor: '.title()))
    pos = 0
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print(f'\nadicionado ao final da lista...'.title())
    else:
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'\nvalor  inserido com sucesso na posição: {pos} da lista...'.title())
                break
            pos += 1
print('@' * 70)
print(f'\nos valores digirtados e colocados em ordem foram:{valores}'.title())
print()
print('@' * 70)





