import random
print('\nDesafio 45 - Jogo Jokenpô.')
n = str(input('\nQual o seu nome?:'))
while True:
    jg = str(input('\nOlá {}, o que você escolhe?'
                   '\n - Pedra,  - Papel,  - Tesoura:'.format(n)))
    n1 = 'pedra'
    n2 = 'papel'
    n3 = 'tesoura'
    lista = [n1, n2, n3]
    pc = random.choice(lista)
    if (pc == n1 and jg == n2) or (pc == n2 and jg == n3) or (pc == n3 and jg == n1):
        print('\nO computador escolheu {}, e você {}, VOCÊ GANHOU!!!'.format((pc.upper()), (jg.upper())))
    elif (pc == n1 and jg == n3) or (pc == n2 and jg == n1) or (pc == n3 and jg == n2):
        print('\nO computador escolheu {}, e você {}, VOCÊ PERDEU!!!'.format((pc.upper()), (jg.upper())))
    else:
        print('\nOPS! EMPATE!!! - O Computador escolheu {}, e Você {}.'.format((pc.upper()), (jg.upper())))

