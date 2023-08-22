from random import randint

print('\ndesafio 68 - jogo do par ou ímpar!\n'.title())
print('Xx' * 75)
win = 0
while True:

    n = int(input('\ndigite um valor: '.title()))
    cpu = randint(0, 10)
    total = n + cpu
    pi = ' '
    while pi not in 'PI':
        pi = str(input('\nvocê quer par ou ímpar? [P/I]: ')).strip().upper()[0]
    print(f'\nvocê jogou {n} e o computador jogou {cpu}, o total foi {total}, '.upper(), end='')
    print('deu par.'.upper() if total % 2 == 0 else 'deu ímpar.'.upper())
    if total % 2 == 0:
        if pi == 'P':
            print('\nvocê venceu!!!'.upper())
            win += 1
        else:
            print('\nvocê perdeu!!!'.upper())
            break
    elif total % 2 ==1:
        if pi == 'I':
            print('\nvocê venceu!!!'.upper())
            win += 1
        else:
            print('\nvocê perdeu!!!'.upper())
            break
    print('\njogue novamente...'.upper())
print(f'\ngame over - você venceu {win} vezes!!!'.upper())



