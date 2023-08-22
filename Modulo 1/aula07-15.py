print('\nDesafio 15 - Calculo de aluguel de carros.')
dias = int(input('\nQuantos dias alugado?: '))
km = int(input('\nQuantos KM rodados?(Arredonde): '))
calc = dias * 60
calc2 = km * 0.15
print('\nO valor a ser acertado por {} dia(s), e {}KM rodados é de: R${:.2f}.'.format(dias, km, calc+calc2))
