print('\nDesafio 09 - Tabuada.')
n = float(input('\nDigite um numero e veja sua tabuada: '))
for c in range(1, 11):
    res = c * n
    print('{} x {} = {}'.format(n, c, res))
