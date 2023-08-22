print('\ndesafio 89 - alunos e média.'.title())
boletins = []
nomes = []
medias = []
notas = []
while True:
    nomes = str(input('\nNome Do Aluno: '.title()))
    nota1 = float(input('\nNota 1: '))
    nota2 = float(input('\nNota 2: '))
    medias = (nota1 + nota2) / 2
    boletins.append([nomes, [nota1, nota2], medias])
    continuar = str(input('\nquer continuar? [S/N]: '.title())).strip()[0]
    if continuar in 'Nn':
        break
print('@' * 26)
print('Nº    NOME          MEDIA')
print('@' * 26)
print()
for i, a in enumerate(boletins):
    print(f'{i}    {a[0]}          {a[2]}'.title())
print()
print('@' * 60)
while True:
    opc = int(input('\nqual aluno você quer ver as notas novamente?: (777 para sair)'.title()))
    print()
    print('@' * 60)
    if opc <= len(boletins) - 1:
        print(f'\nas notas de {boletins[opc][0]}, são:{boletins[opc][1]}.'.title())
        print()
        print('@' * 60)
    if opc == 777:
        break
print('xX' * 12, 'FIM!!!', 'Xx' * 12)
print('@' * 60)
