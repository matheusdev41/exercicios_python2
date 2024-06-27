n = []
res = ''
count = 0
while True:
    n.append(int(input('Digite um valor: ')))
    res = str(input('Deseja continuar?[S/N]: '))
    if 'n' in res:
        break
    if 5 in n:
        count += 1
    else:
        print('O valor 5 não apareceu na lista')
print('O valor 5 apareceu na lista {} vezes'.format(count))
print('Os números digitados foram {}'.format(n))
print('A quantidade de números digitados foram {}'.format(len(n)))

