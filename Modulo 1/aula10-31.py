print('Desafio 31 - Preço de Passagens'
      '\n\nAté 200KM , R$0.50 por KM, \nacima de 200KM, R$0.45 por KM.')
while True:
    km = int(input('\nQual a distância de sua viagem?:'))
    if km <= 200:
        print('\nSua viagem custará R${:.2f}'.format(km * 0.50))
    else:
        print('\nSua viagem custará R${:.2f},com R$0.05 centavos de desconto por KM!'.format(km * 0.45))
