print('\nDesafio 40 - Média, aprovado ou reprovado!')
n = str(input('\nQual é o seu nome?:'))
m1 = float(input('\nOlá {}, vamos saber se você foi aprovado?'
                 '\n\nQual a sua média em exatas?:'. format(n)))
m2 = float(input('Qual a sua média em humanas?:'))
soma = (m1 + m2) // 2
if soma < 5.0:
    print('\nSua média foi {:.2f}, infelizmente você foi reprovado.'.format(soma))
elif soma >= 5.0 and soma <= 6.9:
    print('\nSua média foi {:.2f}, você está de recuperação!'.format(soma))
elif soma >= 7.0:
    print('\nSua média foi {:.2f}, parabéns, você foi aprovado!'.format(soma))
else:
    print('\nVocê digitou valores incorretos tente novamente! ')
print('\n\n', 'X' * 40, 'FIM!!', 'X' * 100)


