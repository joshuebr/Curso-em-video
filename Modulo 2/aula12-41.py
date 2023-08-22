import datetime
print('\nDesafio 41 - Cassificação de Atletas de Natação.')
n = str(input('\nQual é o seu nome?:'))
i = int(input('\nOlá {}, qual o ano de seu nascimento?:'.format(n)))
tempo = datetime.datetime.today().year
t = tempo - i
if t <= 9:
    print('\n{}, Você tem {} ano(s) e pertece a classificação MIRIM.'.format(n, t))
elif t >= 10 and t <= 14:
    print('\n{], Você tem {} ano(s) e pertence a classificação INFANTIL.'. format(n, t))
elif t >= 15 and t <= 19:
    print('\n{}, Você tem {} ano(s) e pertence a classificação JUNIOR.'.format(n, t))
elif t == 20:
    print('\n{}, Você tem {} ano(s) e pertence a classificação SÊNIOR.'.format(n, t))
else:
    print('\n{}, Você tem {} ano(s) e pertence a classificação MASTER.'.format(n, t))
print('\n\n', '_' * 40, 'FIM!!!', '_' * 100)