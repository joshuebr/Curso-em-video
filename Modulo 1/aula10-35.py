print('\nDesafio 35 - Seus segmentos de retas formam um triâgulo?')
r1 = float(input('\nInsira primeira reta:'))
r2 = float(input('\nInsira a segunda reta:'))
r3 = float(input('\nInsira a terceira reta:'))
if r2 + r3 > r1 and r1 + r3 > r2 and r1 + r2 > r3:
      print('\nSim, seus seguimentos podem formar um triângulo!\n\n FIM!!!\n')
else:
      print('\nNão, seu seguimentos não podem formar um triângulo!\n\n FIM!!!\n')