print('\nDesafio 57 - Lendo a entrada correta do sexo "M" ou "F".')
s = 'M' or 'F'
s = str(input('\nPor favor digite seu sexo ( M ou F): ')).upper()
while s != 'M' and s != 'F':
    print('\nPor favor, digite somente como pedido, "M" ou "F".', end= ' ')
    s = str(input()).upper();
print('\nvocê digitou correto!!'.upper())
print('\n','xX' * 40, 'FIM!!!', 'Xx' * 100)

