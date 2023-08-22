print('\ndesafio 77 - mostrando palavras e suas vogais!'.title())
tupla = ('Mercado', 'Japones', 'Salame', 'Mulher', 'Cinco', 'Dezenove', 'Sete', 'Triturar', 'Comboio', 'Escola')
for vogal in tupla:
    print(f'\nna palavra {vogal}, temos: '.title(), end='')
    for letra in vogal:
        if letra.lower() in 'aeiou':
            print(letra.lower() , end=' <- ')