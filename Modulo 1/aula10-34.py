print('\nDesafio 34 - Cálcular Aumento de Salário.')
salario = float(input('\nDigite o valor do seu salário:'))
if salario > 1250:
    salario1 = (salario / 100 * 10) + salario
    print('\nSeu salário pode ser aumentado até {:.2f}.\n\nFIM!!!'.format(salario1))
else:
    if salario <= 1250:
        salario2 = (salario / 100 * 15) + salario
        print('\nSeu salário pode ser aumentado até {:.2f}.\n\nFIM!!!'.format(salario2))
