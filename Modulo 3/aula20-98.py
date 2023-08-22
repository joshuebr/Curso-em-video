from time import sleep

print('\nDesafio 98 - Contagens Regressivas Diferenciadas.')


def cont(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print()
    print('xX' * 20)
    print(f'Contagem comum de {i} a {f}, de {p} em {p}:')
    if i < f:
        conta = i
        while conta <= f:
            print(f'{conta} ', end='')
            sleep(0.25)
            conta += p
        print('FIM!!')
    else:
        conta = i
        while conta >= f:
            print(f'{conta} ', end='')
            sleep(0.5)
            conta -= p
        print('FIM')
    print('xX' * 20)


# main
cont(1, 10, 1)
cont(10, 0, 2)
print('\nAgora é sua vez de personalizar a contagem')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
cont(i, f, p)
