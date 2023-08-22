print('\n Desafio 11 - Medidas para pinturas.\n')
larg = int(input('Qual a largura do local?\n'))
alt = int(input('Qual a altura do local?\n'))
calc = larg * alt
print('Seu local mede {} metros quadrados.\n'.format(calc))
tinta = 2
calc2 = calc / tinta
print('e precisa de {} litros de tinta!\n FIM!'.format(calc2))