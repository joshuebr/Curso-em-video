print('\ndesafio 67 - tabuada v3.0.'.title())
while True:
    tab = 0
    op = 1
    result = 0
    n = int(input('\ndigite um número e veja sua tabuada: '.title()))
    print('=' * 37)
    if n < 0 :
       break
    while tab != 10:
        tab += op
        result = n * tab
        print(f'|| {n} x {tab} = {result}')
    print('=' * 37)
print('\n"sorry", eu sei calcular com números negativos,' 
    ' mas fui programado pra \nfuncionar somente'
    ' com números positivos inteiros!!!'.upper(),
    '\n\n', 'xX' * 40, 'FIM!!', 'Xx' * 100)




