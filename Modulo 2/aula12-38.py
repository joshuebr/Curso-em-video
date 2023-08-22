print('\nDesafio - 38 - Mostrando qual número é de maior valor. ')
while True:
    n1 = int(input('\nDigite o primeiro número:'))
    n2 = int(input('\nDigite o segundo número:'))
    if n1 > n2:
        print('\nO primeiro valor é maior!')
    elif n1 < n2:
        print('\nO segundo valor é maior!')
    else:
        print('\nNão existe valor maior,'
              'os dois valores são iguais!')
    print('\n','*' * 40, 'FIM!!', '*' * 100)