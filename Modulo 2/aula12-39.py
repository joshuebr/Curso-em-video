import datetime
print('\nDesafio 39 - Alistamento no Exército.'
      '\nVocê está pronto para se alistar?')
n = str(input('\nQual o seu nome?:'))
i = int(input('\nOlá {}, qual o ano que você nasceu?:'.format(n)))
tempo = (datetime.datetime.today().year)
t = tempo - i
if t == 18:
      print('\nVocê já tem, {} ano(s), a idade certa para se alistar!'.format(t))
elif t < 18:
      res = 18 - t
      print('\nVocê ainda tem {} ano(s) e nao tem idade para se alistar, falta(m) {} ano(s).'.format(t, res))
else:
      res2 = t - 18
      print('\nVocê tem {} ano(s), já passou {} ano(s), do prazo de alistamento.'.format(t, res2))
print('\n\n', '-' * 40, 'FIM!!!', '-' * 100)
