print('\ndesafio 66 - lendo e somando números - '
      '\nsó cessará ao digitar [999] - daí somará todos, menos o flag!!!'.title())
print('Xx' * 75)
count = 0
n = 0
soma = 0
while True:
    n = int(input('\nentre com qualquer número inteiro e digite 999 para parar: '.title()))
    if n == 999:
        break
    soma += n
    count += 1
print(f'\nforam digitados {count} números, o resultado da soma entre eles, é {soma}'.upper(), end=' ')
print('fim!!!'.upper())
print('\n', 'xX' * 25, 'FIM!!!', 'Xx' * 75)
