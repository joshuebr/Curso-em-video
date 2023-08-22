print('\nDesafio 26 - Lendo uma frase e mostrando quantas letras "A" aprecem,'
      '\na pimeira e a última posição em que aparecem!\n')
while True:
    frase = input('Escreva uma frase:')
    count = frase.lower().count('a')
    pos_1 = frase.find('a') + 1
    pos_2 = frase.rfind('a') + 1
    if count:
     print('\nSua Frase contem {} letras "A", '
           '\nSua primeira posição é {},'
           '\nSua última posição é:{} \n\nFIM!!\n '.format(count, pos_1, pos_2))
     break
    else:
     print('Entrada inválida!')
