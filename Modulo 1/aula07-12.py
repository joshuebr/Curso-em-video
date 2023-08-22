print('Desafio 12 - descontos em compras !\n')
preco = int(input('Qual o preço do produto?'))
desc = preco / 100 * 5
res = preco - desc
print('\nO valor do produto é {}, seu  desconto de 5%, será de {:.2f}.\n'
      '\nEntão o produto passará a ser de {:.2f}.\nFIM!\n'.format(preco, desc, res))
