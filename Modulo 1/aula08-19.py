import math
import random

print('\nDesafio 19 - Sorteio.\n'
      '\nUm professor precisa escolher um dos\nquatro alunos, '
      'para apagar o quandro, os alunos são:\n'
      '\n1º - Jhon, 2º - Pedro, 3º - Thiago,'
      'e o 4º é você!\n')
a1 = 'Jhon'
a2 = 'Pedro'
a3 = 'Thiago'
voce = input('Então, qual o seu nome?')
print('\nVamos ao sorteio?\n')
lista = [voce, a1, a2, a3]
esc = random.choice(lista)
print('\nO aluno escolhido foi: {}.'
      '\n\nFIM!!'.format(esc))




