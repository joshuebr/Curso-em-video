print('\ndesafio 71 - caixa eletrônico'.title())
print('\n')
print('@' * 37, '\n@@@@@ joshuas tech tecnologia @@@@@@@'.upper())
print('@' * 37)
valor = int(input('\nqual valor deseja sacar?: R$'.title()))
total = valor
ced = 200
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'\ntotal de {totced} cédulas de R${ced}.'.title())
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            print('\nvolte sempre!'.title())
            break
print('\nsimulação encerrada!'.upper())
print('@' * 37, '\n@@@@@ joshuas tech tecnologia @@@@@@@'.upper())
print('@' * 37)
