print('\ndesafio 97 - Textos Sublinhados')
print()


def textos(txt):
    le = len(txt)
    print(le * '@')
    print(f'{txt}')
    print(le * '@')


textos('Olá Mundo!')
textos('Josué Rodrigues Silva!')
textos('Curso de Python no YouTube!')
textos('CeV')
user = str(input('\nAgora escreva seu texto simples: ')).title()
print()
textos(user)
