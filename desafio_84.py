tem = []
pri = []
res = ''
mai = men = 0
while True:
    tem.append(str(input('Nome: ')))
    tem.append(float(input('Peso: ')))
    pri.append(tem[:])
    if len(tem) == 0:
        mai = men = tem
    else:
        if tem[1] > mai:
            mai = tem[1]
        if tem[1] < men:
            men = tem[1]
    tem.clear()
    res = str(input('Deseja continuar[S/N]: '))
    if res in 'Nn':
        break
print('='*30)
print('A quantidade de pessoas cadastradas foi:\n'
      '{}'.format(len(pri)))
for p in pri:
    if p[1] == mai:
        print('{}'.format(p[0]))



