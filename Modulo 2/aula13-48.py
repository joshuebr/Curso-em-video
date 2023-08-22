from time import sleep
print('\nDesafio 48 - Calculando a soma entre todos os'
      '\nnúmeros ímpares que são múltiplos de três, entre 1 - 500. ')

i = str(input('\nPara iniciar, escreva a palavra sim !!'))

while(i != str):
      print("\nEscreva a palavra SIM!!!", end= ' ')
      i = str(input());

      if i == 'sim' or i == 'Sim' or i == 'SIM':
            soma = 0
            cont = 0
            print('\nIniciando...')
            sleep(1)
            print('\nDe 1 a 500...')
            sleep(1)
            print('\nEncontrando valores...')
            sleep(1)
            print('\nCalculando...')
            sleep(1)
            print('\nResultado:')
            sleep(0.5)
            for n in range (1, 501, 2):
                  if n % 3 == 0:
                        cont = cont + 1
                        soma = soma + n
            print('\nTodos os {} valores, somam {}.'.format(cont, soma),
             '\n\n', 'xX' * 20, 'FIM!!', 'Xx' * 100)
            sleep(1)
            break







