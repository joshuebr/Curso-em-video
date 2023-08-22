print('\nDesafio 27 - Lendo um nome e separando \no primeiro e último nome.\n')
while True:
    nome = str(input('\nDigite um nome completo:')).strip()
    n = nome.split()
    n2 = nome.replace(" ", "").isdigit()
    if n2:
        print('\nPor favor digite apenas palavras!!!\n')
    else:
         print('\nPrazer em conhecer {}!'.format(n[0].title()))
         print('\nSeu primeiro nome é {}!'.format(n[0].title()))
         print('\nSeu último nome é {}!'.format(n[-1].title()))
         break
