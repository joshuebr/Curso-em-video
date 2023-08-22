from unicodedata import normalize
print('\nDesafio 53 - Frases em Palídromo.')
frase = str(input('\nDigite uma frase: ')).strip().upper()
palavras = frase.split()
troca = ''.join(palavras)
inverter = ''
for letra in range(len(troca) - 1, - 1, - 1):
    inverter += troca[letra]
if inverter == troca:
    print('\033[32m\n{} - {},'.format(troca, inverter),
          'Sua frase é um palíndromo!!!')
else:
    print('\033[31m\n{} - {},'.format(troca, inverter),
          'Sua frase não é um palíndromo!!!')
print('xX' *40, 'FIM!!!!', 'Xx' *100, end= '')