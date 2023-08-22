print('\ndesafio 72 - imprimindo por extenso um numero digitado!'.title())
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

n = int(input('\ndigite um número entre 0 e 20: '.title()))
while n > 20 or n < 0:
    print(f'\ntente novamente: '.upper(), end='')
    n = int(input())
if n <= 20 or n >= 0:
    n = tupla[n]
    print('\no número escolhido, escrito por extenso é:'.title(), n.upper())
