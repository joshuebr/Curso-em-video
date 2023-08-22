print('\ndesafio 94 - pessoas, sexo e idades.'.title())
nome = list()
sexo = list()
idade = list()
pessoas = dict()
totpes = 0
id = 0
mulheres = list()
acima = 0
while True:
    totpes += 1
    nome.append(str(input('\nNome: ')))
    sexo.append(str(input('\nSexo [F/M]: ').upper().strip()[0]))
    idade.append(int(input('\nIdade: ')))
    continuar = str(input('\nDeseja continuar [S/N]?:')).strip()[0]
    if continuar in 'Nn':
        break
pessoas['nomes'] = nome[:]
pessoas['sexo'] = sexo[:]
pessoas['idade'] = idade[:]
print(pessoas)
mulheres.append(pessoas.copy([sexo]))
print(mulheres)
for p, i in enumerate(pessoas['idade']):
    id += i
print('@' * 40)
print(f'\nO grupo tem {totpes} pessoa(s).'
      f'\nA média de idade é de {id / totpes}.'
      f'\nAs mulheres cadastradas foram: ', end='')
for y in range(0, len(mulheres)):
    if mulheres[y]['sexo'] == 'F':
        print(mulheres[y]['nome'], end='')
