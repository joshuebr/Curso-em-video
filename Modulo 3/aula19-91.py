from random import randint
from time import sleep
from operator import itemgetter
print('\ndesafio 91 - jogos de dados.'.title())
players = {}
num = []
rank = {}
rerank ={}
print('@' * 37)
print('       LANÇANDO OS DADOS.')
print('@' * 37)
players = {f'Jogador -> 1': randint(1, 6),
           f'Jogador -> 2': randint(1, 6),
           f'Jogador -> 3': randint(1, 6),
           f'Jogador -> 4': randint(1, 6)}
for k, v in players.items():
    print(f'\npara o {k}, caiu o nº{v}.'.title())
    sleep(0.90)
rank = sorted(players.items(), key=itemgetter(1), reverse=True)
print('@' * 37)
print('       RESULTADO DOS LANÇAMENTOS')
print('@' * 37)
for j, n in enumerate(rank):
    print(f'\nem {j+1}º lugar: {n[0]} com o {n[1]}'.title())
    sleep(0.90)
