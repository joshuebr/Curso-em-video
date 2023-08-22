print('\ndesafio 75 - inserindo quatro valores em uma tupla.'.title())
n = (int(input('\ndigite um valor:')),
     int(input('\ndigite um valor:')),
     int(input('\ndigite um valor:')),
     int(input('\ndigite um valor:')))
print(f'\nvocê digitou os valores: {n}'.title())
print(f'\no valor 9 apareceu {n.count(9)} vezes.'.title())
if 3 in n:
     print(f'\no valor 3 foi digitado na posição {(n.index(3) + 1)} primeiro.')
else:
    print('\no valor 3 não foi digitado.'.upper())
print('\nos valores pares digitados foram : '.title(), end='')
for i in n:
     if i % 2 == 0:
          print(f'{i}',  end=' <- ')




