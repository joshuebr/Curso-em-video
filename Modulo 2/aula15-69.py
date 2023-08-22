print('\ndesafio 69 - cadastramento de pessoas.'.title())
print('xX' * 60)

somidade = 0
novinhas = 0
homens = 0
while True:
    print('+' * 37, '\n++++++++ cadastre uma pessoa ++++++++'.title())
    print('+' * 37)
    idade = int(input('idade: '.title()))
    if idade > 18:
        somidade += 1
    sexo = ' '
    while sexo not in 'MFmf':
        sexo = str(input('sexo = [M/F]: ')).title().strip()[0]
    if sexo == 'M':
        homens += 1
        print('+' * 37)
    elif sexo == 'F' and idade < 20:
        novinhas += 1
    res = ' '
    while res not in 'SN':
        res = str(input('\nquer continuar a cadastrar? [S/N]: ')).title().strip()[0]
    if res == 'N':
        print('\nacabou...'.title())
        sleep(0.5)
        break


print('+++++++ fim do cadastramento ++++'.upper())
print('+' * 120)
print(f'\nao todo temos {somidade} pessoa(s) com mais de 18 anos,'
     f' são {homens} homen(s) cadastrados e temos {novinhas} mulher(es) com menos de 20 anos.'.title())
print('+' * 120)