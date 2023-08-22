print('\nDesafio 01 - calculando a compra de uma casa.')
while True:
    casa = float(input('\nQual o valor da casa?: R$'))
    salario = float(input('\nQual o valor do seu salário?: R$'))
    tempo = float(input('\nQuantos anos você quer financiar?:'))
    if (casa / (tempo * 12)) > (salario / 100 * 30):
        print('\nInfelizmente não podemos conceder o empréstimo!')
    elif (casa / (tempo * 12)) < (salario / 100 * 30):
        print('\nSeu empréstimo foi pré aprovado, com parcelas de '
              '{}x de R${:.2f}.'.format(int(tempo * 12), (casa / (tempo * 12))))
    print('\nObrigado e volte sempre.')
