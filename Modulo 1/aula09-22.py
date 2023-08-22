print('Desafio 22 - Lendo um nome completo, mostrando:\n'
      '\nTodas as letras maiúsculas,'
      '\nTodas as letras minúsculas,'
      '\nQuantas letras ao todo, sem espaços,'
      '\nQuantas letras tem o primeiro nome.\n'
      '\nVamos lá?\n')
while True:
      nome = str(input('Digite seu nome:'))
      if not nome.isalpha():
          print('\nEntrada inválida, digite apenas letras.!\n' )
      else:
       print('Seu nome em maiúsculas, ficaria assim:', nome.upper())
       print('Seu nome em minúsculas, ficaria assim:', nome.lower())
       print('Seu nome escrito corretamente seria:', nome.title())
       print('Seu nome contém esta quantidade de letras:', len(nome.replace(" ", "")))
       pri_nom = nome.split()
       print('Seu primeiro nome contém esta quantidade de letras:', len(pri_nom[0]))
       print('\n\nFIM!\n')
       break
