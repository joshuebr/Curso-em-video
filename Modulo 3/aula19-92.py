from datetime import datetime
print('\ndesafio 92 - dados trabalhistas.'.title())
print('@' * 40)
print(f'       bem vindo ao rh!'.upper())
print('@' * 40)
empregado = dict()
empregado['nome'] = str(input('\nqual é o seu nome?: '.title())).title()
DN = int(input('\nano de nascimento: '.title()))
empregado['idade'] = datetime.now().year - DN
empregado['CTPS'] = int(input('\ncarteira de trabalho -> (0 = não tem): '.title()))
if empregado["CTPS"] <= 0:
    print(f'\no candidato {empregado["nome"]}, tem {empregado["idade"]} anos e não tem CTPS.'.title())
else:
    empregado['contratação'] = int(input('\nano de contratação: '.title()))
    empregado['aposentadoria'] = (35 - (datetime.now().year - empregado['contratação'])) + empregado["idade"]
    empregado['salario'] = int(input('\nSalário: '))
    print(f'\no candidato se chama {empregado["nome"]}, tem {empregado["idade"]} anos.'
          f'\nsua CTPS é de Nº{empregado["CTPS"]}. sua primeira contratação foi no ano de {empregado["contratação"]}.'
          f'\ncom salário de R${empregado["salario"]:.2f}. e irá se aponsentar com {empregado["aposentadoria"]}'
          f' anos.'.title())
