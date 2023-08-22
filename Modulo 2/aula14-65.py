print('\ndesafio 65 - lendo números inteiros - mostrando a média,'
      '\nqual foi o maior e o menor, e opções de continuar.'.title())
print('Xx' * 75)
count = 0
media = 0
n = 0
x = 0
maior = 0
menor = 0
opcao = 'Ss'

while opcao in'Ss':
     n = int(input('\ndigite números inteiros: '.title()))
     count += n
     x += 1
     media = count / x
     if x == 1:
         maior = n
         menor = n
     else:
          if n > maior:
                  maior = n
          elif n < menor:
                   menor = n
     opcao = str(input('\ngostaria de continuar?[S/N]: '.title()))
print('\na média dos números são: {:.2f}!'
            '\n\no número maior é {}, e o menor é {}!'.upper().format(media, maior, menor))
print('\n', 'xX' * 25, 'FIM!!!', 'Xx' * 75)
