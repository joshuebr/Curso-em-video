print('\nDesafio 42 - Qual tipo de triângulo será formado?')
while True:
    r1 = float(input('\nInsira a primeira reta:'))
    r2 = float(input('\nInsira a segunda reta:'))
    r3 = float(input('\nInsira a terceira reta:'))
    #condições aninhadas
    if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
        print('\nSim, suas retas formam um triângulo.', end='')
        if r1 == r2 == r3:
            print('Ele seria EQUILÁTERO.')
        elif r1 != r2 != r3 != r1:
            print('Ele seria ESCALENO.')
        else:
            print('Ele seria ISÓSCELES.')
    else:
        print('\nNão, suas retas não formariam um triângulo.')

