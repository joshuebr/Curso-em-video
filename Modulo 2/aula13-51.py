print('\nDesafio 51 - Progressão Aritmética, primeiro termo e razão!!')

t = int(input('\nDigite o 1º termo: '))
r = int(input('\nDigite a razão: '))
dec = t + (11 - 1) * r
for x in range(t, dec, r):
    print('{} '.format(x), end=' =>')
print(' FIM!!!')

