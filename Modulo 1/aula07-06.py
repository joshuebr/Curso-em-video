print('\nDesafio 6.Digitando um numero e mostrando \no seu dobro, triplo e raiz quadrada.')
nu1 = int(input('Digite um número:'))
mul1 = nu1 * 2
pot1 = nu1 ** 2
raq1 = nu1 ** (1/2)
mul2 = nu1 * 3
pot2 = nu1 ** 3
raq2 = nu1 ** (1/3)

print('\nO número que você escolheu é: {}\nSeu dobro é: {}\nSeu triplo é: {}'
      '\nSua potência ao quadrado é: {}\nSua potência ao cubo é: {}\nE por fim,'
      'sua raiz quadrada é: {:.2f}'.format(nu1, mul1, mul2, pot1, pot2, raq1))
print('\nSe fosse raiz cúbica, seria: {:.2f}\n \nFim!'.format(raq2))

