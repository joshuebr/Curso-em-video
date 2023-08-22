print('\ndesafio 73 - tabela de colocados brasileirão !'.title())
times = ('Cruzeiro', 'Atlético', 'América', 'Vila Nova', 'Corinthians',
         'São Paulo', 'Santos', 'Grêmio', 'Chapecoense', 'Palmeiras',
         'Paraná', 'Bahia', 'Internacional', 'Flamengo', 'Fluminense')
print('\nlista de times do brasileirão: '.title(), times)
print('\nos 5 primeiros colocados são: '.title(), times[0:5])
print('\nos 4 últimos colocados são : '.title(), times[-4:])
print('\ntimes em ordem alfabética: '.title(), sorted(times))
print(f'\no {times[8].title()}, está na {times.index("Chapecoense")}ª posição! '.title())
