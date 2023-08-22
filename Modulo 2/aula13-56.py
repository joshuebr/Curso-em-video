print('\nDesafio 56 - Média de idade, nome do homem mais velho,'
      ' mulheres com menos de 20 anos.')
somaidade =0
maisvelho = 0
novinhas = 0
tiozao = 0
for i in range(1, 5):
    nomes = str(input('\nQual o nome da {}ª pessoa?:'.format(i)))
    idades = int(input('\nQual a idade da {}ª pessoa?:'.format(i)))
    sexos = int(input('\nQual o sexo da {}ª, pessoa? [ 1 = M, 2 = F ]:'.format(i)))

    if idades == 1:
        maisvelho = idades
    else:
        if idades > maisvelho and sexos == 1:
            maisvelho = idades
            tiozao = nomes

    if idades > 1:
        somaidade += idades
    else:
        if idades + somaidade:
            somaidade = idades

    if sexos == 2 and idades < 20:
        novinhas += 1

print('\n\nA média de idade do grupo é {:.2f}!'
      '\n\nO homem mais velho é {}, com {} anos!'
      '\n\nExistem {}, mina(s) com menos de 20 anos!'.format(somaidade / 4, tiozao.upper(), maisvelho, novinhas))
print('\n','xX'*40, 'FIM!!', 'Xx'*100, end= '')
