print('\nDesafio 32 - Informar se o ano é Bissexto.')
while True:
    ano = int(input('\nQual o ano que gostaria de saber?:'))
    if (ano % 4) == 0:
        print('\nSim, o ano de {}, é Bissexto!'.format(ano))
    else:
        print('\nNão, o ano de {}, não é Bissexto.'.format(ano))
