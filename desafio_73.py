tim = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo',
        'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional',
       'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro',
       'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
print('Os primeiros 5 colocados foram {}'.format(tim[:5]))
print('='*20)
print('Os últimos 4 colocados foram {}'.format(tim[20:15:-1]))
print('='*20)
print('Os times em ordem alfabética são {}'.format(sorted(tim)))
print('='*20)
print('O time do Cruzeiro está na posição {}'.format(tim.index('Cruzeiro')))
