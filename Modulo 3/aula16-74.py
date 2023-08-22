from random import randint
import random
print('\ndesafio 74 - sorteando números em uma tupla vazia,'
      '\n mostrando maior e nenor inserido!'.title())
tupla = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),
print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#print('\n')
print('os números sorteados foram: ', end='')
for x in tupla:
    print(f'{x} ', end='')
print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

print(f'\no maior número foi {max(tupla)},'
      f'\n\ne o menor foi {min(tupla)}.'.title())
print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
