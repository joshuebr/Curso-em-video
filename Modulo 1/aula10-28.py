import random
print('\nDesafio 28 - Adivinhe o que estou pensando.\n ')
while True:
    n = int(input('\nQual o numero estou pensando, de 1 a 5?:'))
    n1 = '1'
    n2 = '2'
    n3 = '3'
    n4 = '4'
    n5 = '5'
    pen = [n1, n2, n3, n4, n5]
    esc = int(random.choice(pen))
    if n == esc:
        print('\nParabéns, estava pensando no número {}!\n FIM!! \n'.format(esc))
        break
    else:
        print('\nSinto muito, mas você errou, estava pensando no número {}!\n'.format(esc))

