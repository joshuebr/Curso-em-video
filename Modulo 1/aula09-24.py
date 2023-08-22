print('\nDesafio 24 - Lendo o nome de uma cidade e \nverificando se começa ou não com o nome "Santo".')
while True:
      cid = input('\nQual o nome da cidade?:')
      #cid.lower()
      if cid.replace(' ', '').lower().find('santo') == False:
       print('\nSim, sua cidade começa com o nome "Santo"!\n\nFIM!!!\n')
       break
      else:
       print('\nNão, sua cidade não começa com o nome "Santo"!')





