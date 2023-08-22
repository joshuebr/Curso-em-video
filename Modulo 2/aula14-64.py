print('\ndesafio 64 - lendo e somando números - '
      '\nsó cessará ao digitar [999] - daí somará todos, menos o flag!!!'.title())
print('Xx' * 75)
count = 0
n = 0
soma = 0
while n != 999:
    soma += n
    count += 1
    n = int(input('\nentre com qualquer número inteiro: '.title()))
    if n == 999:
        count -= 1
print('\nforam digitados {} números, o resultado da soma entre eles, é {}'.upper().format(count, soma), end=' ')
print('fim!!!'.upper())
print('\n', 'xX' * 25, 'FIM!!!', 'Xx' * 75)
