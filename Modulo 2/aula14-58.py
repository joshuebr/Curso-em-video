import random
import sys
print('\nDesafio 58 - Qual número o computador está pensando??')
try:
    i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = random.choice(i)
    cont = 1
    cpu = int(input('\nCOMPUTADOR: Qual número estou pensado de 0 a 10?: '))
    while res != cpu:
        print('\nvocê errou, estava pensando no número {}.'
         '\ntente denovo:'.upper().format(res), end= ' ')
        cpu = int(input())
        res = random.choice(i);
        cont += 1
    print('\nparabéns, você acertou, estava pensando no número {},'
      '\nvocê usou {} tentativas!.'.upper().format(res, cont))
except ValueError:
    print('\nValores inválidos!!',
          '\n\n', 'xX' * 40, 'FIM!!', 'Xx' * 100)
    sys.exit(1)

