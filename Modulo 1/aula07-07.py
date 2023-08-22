print('\nDesafio 7. Inserindo notas de alunos \ne calculando a média.\n')
mat = int(input('\nDigite a nota de Matemática:'))
print('Sua nota de Matemática é: {} pontos.\n'.format(mat))
port = int(input('\nDigite a nota de Português:'))
print('Sua nota de Português é: {} pontos.\n'.format(port))
soma = mat + port
print('A soma das duas notas são: {} pontos.\n'.format(soma))
med = (mat + port) // 2
print('Sua média entre as notas é de:{}.\n'.format(med))
