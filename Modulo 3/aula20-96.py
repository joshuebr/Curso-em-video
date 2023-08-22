print('\ndesafio 96 - funções - Controle de Terreno.')


def area(a, b):
    m = a * b
    print(f'\nA área de um terreno {a} x {b} é de {m}m2.')

def titulo():
    print('@' * 40)
    print('         Controle de Terrenos')
    print('@' * 40)


titulo()
a = float(input('\nLargura do Terreno?: '))
b = float(input('\nCumprimento do terreno?: '))
area(a, b)
