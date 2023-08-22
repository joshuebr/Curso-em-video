print('\nDesafio 43 - IMC - Índice de massa corporea.')
n = str(input('\nQual seu nome?:'))
i = int(input('\nOlá {}, qual sua idade?:'.format(n)))
a = float(input('\nQual sua altura?:'))
p = float(input('\nQual o seu peso?:'))
f = p // (a**2)
print('\nSeu IMC é de {}.'.format(f))
if (f >= 18.5) and (f <= 25.0):
    print('\nVocê está com o peso ideal!')
elif (f >= 26.0) and (f <= 30.0):
    print('\nVocê está com sobrepeso, cuide-se!')
elif (f >= 31.0) and (f <= 40.0):
    print('\nVocê está com obesidade, procure ajuda médica!')
elif (f > 40.0):
    print('\nVocê está com obesidade morbida, regime e ajuda médica urgente!')
else:
    print('\nVocê está abaixo do peso!')

print('\n\n', '@' * 40, 'FIM!!!', '@' * 100)
