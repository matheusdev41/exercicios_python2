lis = (int(input('Digite um valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite mais um valor: ')),
       int(input('Digite mais um valor:  ')))
print('Os valores digitados foram {}'.format(lis))
if 9 in lis:
    print('O número 9 apareceu {} vezes'.format(lis.count(9)))
else:
    print('O número 9 NÃO APARECEU')
if 3 in lis:
    print('O número 3 apareceu primeiro na posição {}'.format(lis.index(3)))
for n in lis:
    if n % 2 == 0:
        print(n, end=' ')






