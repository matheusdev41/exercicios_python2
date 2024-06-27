notas = [] #SEMPRE É NECESSÁRIO CRIAR UMA LISTA VAZIA

n1 = float(input('N1: '))
while (n1 > 10) or (n1 < 0): #ENQUANDO N1 FOR MAIOR QUE 10 OU MENOR QUE 0
    print('NOTA INVÁLIDA')
    n1 = float(input('N1: ')) #PEÇA O DADO NOVAMENTE

notas.append(n1) #CASO PASSE O WHILE, ADICIONE NOTAS A LISTA

n2 = float(input('N2: '))
while (n2 > 10) or (n2 < 0): #ENQUANTO N2 FOR MAIOR QUE 10 OU MENOR QUE 0
    print('NOTA INVÁLIDA')
    n2 = float(input('N2: ')) #PEÇA O DADO NOVAMENTE

notas.append(n2) # CASO PASSE O WHILE, ADICIONE NOTAS A LISTA

n3 = float(input('N3: '))
while (n3 > 10) or (n3 < 0)
    print('NOTA INVÁLIDA')
    n3 = float(input('N3: '))

notas.append(n3)

media = (n1 + n2 + n3) / 3

print(notas)
print(f'Sua média foi {media}')
if media >= 6: # SE A NOTA FOR MAIOR OU IGUAL A 6
    print('Você foi aprovado')
else:
    print('Você foi reprovado')



