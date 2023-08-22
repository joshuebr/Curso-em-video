print('\ndesafio 93 - aproveitamento de um jogador de futebol.')
print('@' * 40)
print(f'   bem vindo ao administração Técnica!'.upper())
print('@' * 40)
jogador = dict()
cont = 0
jg = list()
jogador['nome'] = str(input('\nQual o nome do jogador?: ')).title()
partidas = int(input(f'\nQuantas partidas {jogador["nome"]} jogou?: '))
print('@' * 40)
while True:
    cont += 1
    # criando uma lista para transformar em dict.
    jg.append(int(input(f'\nQuantos gols na {cont}ª partida?: ')))
    if cont == partidas:
        break
jogador['gols'] = jg[:]  # transformando a linha em dict.
jogador['total'] = 0
print('@' * 40)
print(f'\nO jogador {jogador["nome"]} jogou {partidas} partida(s).')
for p, g in enumerate(jogador['gols']):
    print(f'\n  -> Na {p+1}ª partida, ele fez {g} gols.')
    jogador['total'] += g
print(f'\nNo total foram {jogador["total"]} gols.')
print('@' * 40)
print(f'           FIM!!!'.upper())
print('@' * 40)
