n = list()
res = ''
while True:
    num = int(input('Digite um valor: '))
    if num not in n:
        n.append(num)
        print('Número registrado com sucesso...')
        res = str(input('Deseja continuar [S/N]? ')).lower()
    else:
        res = str(input('Número já registrado, deseja continuar [S/N]? '))
    if 'n' in res:
        break
print('='*30)
print('Os números digitados foram {}'.format(sorted(n)))



