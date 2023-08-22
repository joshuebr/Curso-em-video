print('\nDesafio 25 - Lendo um nome e expecificando \nse contém a palavra "Silva"!\n')
while True:
      nome = input('Qual o nome desejado?:')
      #nome.lower()
      if 'silva' in nome.lower():
       print('\nSim, o nome possui a palavra "Silva"!\n\nFIM!!!\n')
       break
      else:
       print('\nNão, o nome não possui a palavra "Silva"\n!')
