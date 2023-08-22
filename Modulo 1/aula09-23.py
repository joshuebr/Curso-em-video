print('\nDesafio 23 - Lendo um número e mostrando'
      ' os digitos seprados!\n')
while True:
    num = int(input('\ndigite um número de 0 a 9999:'))
    if num >= 10000:
        print("\nNumero ou entrada inválida!\n")
    else:
     uni = num % 10
     dez = (num - uni) / 10 % 10
     cen = (num - dez) / 100 % 10
     mil = (num - cen) / 1000 % 10
     uni = int(uni)
     dez = int(dez)
     cen = int(cen)
     mil = int(mil)
     print('\nSeu número é {}, contém {} unidade(s),'
      '{} dezena(s), {} centena(s), {} milhar.\n\nFIM!!!\n'.format(num, uni, dez, cen, mil))
     break