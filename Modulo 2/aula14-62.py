from time import sleep
import sys
print('\ndesafio 62  - progressão aritmética - 10 primeiros termos + opções!'.title())
t = int(input('\ndigite o primeiro termo: '.title()))
r = int(input('\ndigite a razão: '.title()))
print('\n')
termo = t
d = 1
op = 0
opcao = 10
while opcao != 0:
    op = op + opcao
    while d <= op:
        print('{} '.format(termo), end='=> ')
        termo += r
        d += 1
    print('fim!!!'.upper())
    opcao = int(input('\nquantos mais você quer ver?: '.title()))

sleep(0.5)
print('\n', 'xX' * 25, 'FIM!!!', 'Xx' * 75)
