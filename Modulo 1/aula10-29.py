print('\nDesafio 29 - Radar de Velocidade  \nSerá que esta na velocidade certa?')
while True:
    velocidade = int(input('\nQual é a velocidade que você esta dirigindo?:'))
    calc = (velocidade - 80) * 7
    multa = 110 + calc
    if velocidade > 80:
        print('\nVocê está acima da velocidade permitida,\n'
              'você foi multado em R$110.00, \nmais R$7.00 por cada KM '
              'acima da velocidade, totalizando em R${:.2f}.'.format(multa))
    else:
        print('\nParabéns, você está dirigindo dentro das normas!\n\nFIM!!\n')
        break
