print('\ndesafio 85 - 2 listas em 1 - par e ímpar'.title())
lista = []
par = []
impar = []
for c in range(1, 8):
    n = int(input(f'\nDigite o {c}º valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        if n % 2 == 1:
            impar.append(n)
lista.append(par[:])
lista.sort()
lista.append(impar[:])
lista.sort()
for c in lista:
    if c[0] % 2 == 0 and c[1] % 2 == 0:
        lista = par
        par.sort()
        print(f'\nos valores pares digitados foram:{par}'.title())
    else:
        if c[1] % 3 == 1 and c[1] % 3 == 1:
            lista = impar
            impar.sort()
            print(f'\nos valores digitado impares foram: {impar}'.title())