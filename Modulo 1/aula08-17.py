import math

print('\nDesafio 17 - Teorema de Pitágoras!\n')
cat_a = float(input('Qual a medida do cateto maior? (considere como (b))='))
cat_b = float(input('Qual a medida do cateto menor? (Considere como (c))='))
print('Quanto vale a hipotenusa? (Considere como (a)).'
      '\nCalculando (a soma dos catetos é igual\n ao quadrado da hipotenusa) = b² + c² = a²...')
b = math.pow(cat_a, 2)
c = math.pow(cat_b, 2)
res = (b + c)
a = math.sqrt(res)
print('\na² = {:.2f}² + {:.2f}².'
      '\na² = {:.2f} + {:.2f}.'
      '\na² = {:.2f}'
      '\na = √{:.2f}'
      '\na = {:.2f}'
      '\nLogo a hipotenusa vale: {:.2f}.\n\nFIM!\n'.format(cat_a, cat_b, b, c, res, res, a, a))
