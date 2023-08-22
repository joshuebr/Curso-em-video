print('\ndesafio 63 - sequência de fibonacci.'.title())
n = int(input('\nquantos termos você quer mostrar?: '.title()))
penul = 0
ult = 1
print('\n')
print('{} => {}'.format(penul, ult), end=' ')
count = 3
while count <= n:
     termo = ult + penul
     print('=> {}'.format(termo), end=' ')
     penul = ult
     ult = termo
     count += 1
print('=> FIM!!!' )
print('\n' * 2, 'xX' * 40, 'FIM!!!', 'Xx' * 75)

