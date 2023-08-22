print('\ndesafio 76 - listagem de preços :'.title())
tabela = ('Placa - Mãe Asus', 1200,
          'Processador i5', 1200,
          'Memória 16 GB DDR4', 600.00,
          'Placa de Vídeo', 1200,
          'SSD Kingston 240 GB', 200.00,
          'Gabinete Gamer', 350.00,
          'Fonte Real 500', 500,
          'Monitor 24"', 1200,
          'Kit Teclado e Mouse Gamer', 200)
for pos in range(0, len(tabela)):
    if pos % 2 == 0:
        print(f'{tabela[pos]:.<30}', end='')
    else:
        print(f'R${tabela[pos]:>7.2f}')