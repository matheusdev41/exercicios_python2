exp = str(input('Digite uma expressão: '))
lis = []
for sim in exp:
    if sim == '(':
        lis.append('(')
    elif sim == ')':
        if len(lis) > 0:
            lis.pop()
        else:
            lis.append(')')
if lis == 0:
    print('Sua expressão é verdadeira')
else:
    print('Sua expressão é inválida')

