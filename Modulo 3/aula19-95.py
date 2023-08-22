print('\ndesafio 93 - aproveitamento de um jogador de futebol.')
print('@' * 40)
print(f'   bem vindo ao administração Técnica!'.upper())
print('@' * 40)
time = list()
jogador = dict()
partidas = list()
cont = 0
continuar = ''
while True:
    jogador.clear()
    jogador['nome'] = str(input('\nQual o nome do jogador?: ')).title()
    jogos = int(input(f'\nQuantas partidas {jogador["nome"]} jogou?: '))
    partidas.clear()
    print('@' * 40)
    for contador in range(0, jogos):
        partidas.append(int(input(f'\nQuantos gols na {contador+1}ª partida?: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    continuar = str(input('\nDeseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar in 'Nn':
        break
print('@' * 40)
print('Cód ', end='')
for elemento in jogador.keys():
    print(f'{elemento:<15}'.title(), end='')
for chave, valor in enumerate(time):
    print(f'\n{chave:>3}  ', end='')
    for dados in valor.values():
        print(f'{str(dados):<15}', end='')
print()
print('@' * 40)
while True:
    jg = int(input('\nMostrar dados específicos de qual jogador?: '))
    print(f'\nlevantamento do jogador {time[jg]["nome"]}:'.upper())
    for p, g in enumerate(time[jg]['gols']):
        print(f'\n  -> Na {p + 1}ª partida, ele fez {g} gols.')
    prox = str(input('\nDeseja continuar? [S/N]: '))
    if prox in 'Nn':
        break
print()
print('@' * 40)
print(f'           FIM!!!'.upper())
print('@' * 40)
