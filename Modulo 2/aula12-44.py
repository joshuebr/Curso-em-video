import sys
print('\nDesafio 44 - Cálculo de compras.')
try:
    while True:
        v = float(input('\nQual o valor do produto interessado?:'))
        avc = (v / 100) * 10
        acard = (v / 100) * 5
        financard = (v / 100) * 20
        pg = str(input('\nQuais as condições de pagamento?'
                         '\n [1] À vista DIN/CH - [2] À vista Cartão - [3] 2x Cartão - [4] 3x ou mais no Cartão:'))
        if pg == '1':
            print('\nA forma de pagamento em dinheiro ou cheque à vista, terá desconto de 10% = R${:.2f},'
                  '\nseu produto ficará em R${:.2f}.'.format(avc, (v - avc)))
        elif pg == '2':
            print('\nA forma de pagamento no cartão à vista, terá desconto de 5% = R${:.2f},'
                  '\nseu produto ficará em R${:.2f}.'.format(acard, (v - acard)))
        elif pg == '3':
            print('\nA forma de pagamento em 2x no cartão, não haverá descontos e nem juros,'
                  '\nseu produto ficará em R${:.2f}, sendo 2x de R${:.2f}.'.format(v, (v // 2)))
        else:
            print('\nA forma de pagamento no cartào de 3x ou mais, haverá juros de 20% = R${:.2f}.'
                  '\nseu produto ficara em R${:.2f}.'.format(financard, (v + financard)))
except ValueError:
    print('\nVocê digitou valores incorretos!''\n\n', 'X' * 40, 'FIM!!', 'X' * 100)
    sys.exit(1)