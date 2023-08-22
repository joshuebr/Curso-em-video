import datetime
print('\nDesafio 54 - Quais das sete pessoas são maiores que 21 anos?:')
tempo = datetime.datetime.today().year
ac = 0
ab = 0
for c in range(1, 8):
    i = int(input('\nDigite o ano de nascimento da {}ª pessoa: '.format(c)))
    if tempo - i >= 21:
        ac += 1
    elif tempo - i < 21:
        ab += 1
print('\n\33[32m{} pessoas, já são de maiores!!!'.format(ac))
print('Aliás todos que nasceram do ano {} pra abaixo,já são maiores de 21 anos!!!'.format(tempo - 21))
print('\n\33[31m{} pessoas, ainda não são de maiores!!!'.format(ab))
print('Aliás, todos que nasceram do ano {} pra acima, não são maiores que 21 anos!!!'.format(tempo - 21))