print('\ndesafio 61  - progressão aritmética - 10 primeiros termos!'.title())
t = int(input('\ndigite o primeiro termo: '.title()))
r = int(input('\ndigite a razão: '.title()))
print('\n')
termo = t
d = 1
while d <= 10:
   print('{} =>'.format(termo), end=' ')
   termo += r
   d += 1
print('FIM!!')
