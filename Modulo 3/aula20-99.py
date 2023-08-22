from time import sleep

print('\nAnalisando números em funções, indicando quantos numeros é o maior número.')

print()


def maior(*num):
    tam = len(num)
    print('@' * 60)
    print('Analisando valores...')
    if len(num) <= 0:
        num = 0
        print('@' * 60)
        print('Analisando valores...')
        print(f'Foram informados {num} valores.'
              f'\nO maior valor informado foi {num}.')
        print()
        print('FIM!!!')
    else:
        for valor in num:
            print(f'{valor} ', end='')
        print(f'-> Foram informados {tam} valores ao todo! ', end='')
        print(f'\nO maior valor informado foi {max(num)}.')
        sleep(1)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
