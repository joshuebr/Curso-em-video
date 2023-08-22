from time import sleep
print('\ndesafio 59 - várias funções com dois valores.'.title())

esc = 0
n1 =int(input('\nentre com o 1º número:'.title()))
n2 = int(input('\nentre com o 2º número:'.title()))


while esc != 5:
    esc = int(input('\no que deseja fazer com os 2 valores?:'
              '\n1 - somar?'
              '\n2 - multiplicar?'
              '\n3 - saber qual é o maior?'
              '\n4 - entrar com novos valores? '
              '\n5 - sair do programa?\n'.title()))
    if esc == 1:
        soma = n1 + n2
        print('\na soma dos dois valores são {}.'.title().format(soma))
    elif esc == 2:
        mult = n1 * n2
        print('\na multiplicação entre os dois valores são {}.'.title().format(mult))
    elif esc == 3:
        if n1 > n2:
            maior = n1
        else:
            if n1 < n2:
                maior = n2
        print('\no maior valor entre {} e {} é o {}.'.title().format(n1, n2, maior))
    elif esc == 4:
        print('\nentre com novos valores: '.title())
        n1 = int(input('\nprimeiro valor: '.title()))
        n2 = int(input('\nsegundo valor: '.title()))
    elif esc == 5:
        print('\nfinalizando...'.title())
        sleep(0.5)
    else:
         print('\nopção inválida, tente novamente!!'.title())
    sleep(3)
print('\n', 'xX' * 40, 'FIM!!!', 'Xx' * 80)


        






