lis = []
max_valor = 0
men_valor = 0
pma = 0
for v in range(0, 5):
    lis.append(int(input('Digite o valor na posição {}: '.format(v))))
    if v == 0:
        max_valor = men_valor = lis[v]
    else:
        if max_valor < lis[v]:
            max_valor = lis[v]
        if men_valor > lis[v]:
            men_valor = lis[v]
print('Os números digitados foram {}'.format(lis))
print('O maior valor foi {} e o menor foi {}'.format(max_valor, men_valor))