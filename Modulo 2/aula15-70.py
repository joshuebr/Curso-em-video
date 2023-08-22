print('\ndesafio 70 - informações de produtos!'.title())
count = 0
count2 = 0
barato = 0
barato2 = ''
total = 0
print('\n')
print('@' * 37, '\n@@@@@ joshuas tech tecnologia @@@@@@@'.upper())
print('@' * 37)
while True:
    produto = str(input('\nqual produto tem interesse?: '.title())).upper()
    valor = float(input('\npreço: '.title()))
    count2 += 1
    total += valor
    if count2 == 1 or valor < barato:
        barato = valor
        barato2 = produto
    if valor > 1000:
        count += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\ndeseja continuar?[S/N]: '.title())).upper()[0]
    if continuar == 'N':
        print('\n@@@@@ fim das compras! @@@@@'.upper())
        break
print(f'\no total das compras = R${total:.2f}.'
      f'\nfoi encontrado {count} produto(s) com valor acima de R$1.000,00.'
      f'\no produto mais barato inserido foi = {barato2}, que custa R${barato:.2f}.'.title())
