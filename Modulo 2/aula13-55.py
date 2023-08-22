print('\nDesafio 55 - Qual o maior e menor peso entre 05 pessoas?')
pm = 0
pn = 0
for p in range(1, 6):
    peso = float(input('\nQual o peso da {}ª pessoa?: '.format(p)))
    if p == 1:
        pm = peso
        pn = peso
    else:
        if peso > pm:
            pm = peso
        elif peso < pn:
            pn = peso
print('\nO maior peso encontrado foi de {}KG'.format(pm))
print('\nO menor peso encontrado foi de {}KG'.format(pn))