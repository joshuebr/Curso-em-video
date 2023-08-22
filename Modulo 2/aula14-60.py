print('\nalculando o fatorial de qualquer número!!'.title())
n = int(input('\ndigite um número: '.title()))
x = n
m = 1

while x > 0:
    print('{}'.format(x), end=' ')
    print('x' if x > 1 else '=', end=' ')
    m *= x
    x -= 1
print('{}'.format(m))


