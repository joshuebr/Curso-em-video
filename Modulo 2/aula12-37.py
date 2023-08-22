print('\nDesafio 37 - Digitando um número e '
      'escolhendo a base de conversão.')
while True:
    numero = int(input('\nDigite um número inteiro:'))
    print('\nSeu número é:{}.'.format(int(numero)))
    converter = str(input('\nPara qual base você quer converter?\n'
                            '([1] - Binário'
                            ' / [2] - Octal'
                            ' / [3] - Hexadecimal):'))
    if converter == '1':
        esc1 = str(bin(numero))
        print('\nSeu número convertido em Binário é: {}.'.format(esc1[2:]))
    elif converter == '2':
        esc2 = str(oct(numero))
        print('\nSeu número convertido em Octal é: {}.'.format(esc2[2:]))
    elif converter == '3':
        esc3 = str(hex(numero))
        print('\nSeu número convertido em Hexadecimal é: {}.'.format(esc3[2:]))
    else:
        print('\nEscolha inválida, tente denovo!!')
    print('\n','='*40,'FIM!!','='*100)



