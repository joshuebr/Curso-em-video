cor = {'vermelho':'\033[31m',
       'azul':'\033[34m',
       'verde':'\033[4;32m',
       'limpa':'\033[m'}
print('Desafio 13 - Aumento de salário.\n')
sal = int(input('Quanto você ganha?'))
aum = sal / 100 * 15
res = sal + aum
print('\nSeu salário é de {}{}{}, com aumento de 15%, que sera de {}{:.2f}{}.\n'
      '\nSeu salario passará a ser de {}{:.2f}{}.\n\nFIM!\n'.format(cor['vermelho'],sal,cor['limpa'],
                                                                    cor['azul'], aum,cor['limpa'], cor['verde'],res, cor['limpa']))