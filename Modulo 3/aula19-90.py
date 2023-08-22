print('\ndesafio 90 - Lendo nome, média e situação do aluno.'.title())
aluno = {'nome': str(input('\nnome do aluno: '.title())), 'media': float(input('\nqual a média do aluno?: '.title()))}
if aluno["media"] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno["media"] < 7:
    aluno['situação'] = 'Recuperção'
else:
    aluno['situação'] = 'Reprovado'
print(f'\no nome  é {aluno["nome"]}.'
      f'\na média é {aluno["media"]}.'
      f'\na situação é {aluno["situação"]}.'.title())
