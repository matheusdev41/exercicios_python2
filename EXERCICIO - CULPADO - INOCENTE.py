lista = [] #só vai ser adicionado a lista as respostas sim
resp1 = str(input('TELEFONOU PARA A VÍTIMA [S/N]: '))
if 's' in resp1.lower(): #se a resposta for sim
    lista.append(resp1) #ela vai ser contabilizada
resp2 = str(input('ESTEVE NO LOCAL DO CRIME [S/N]: '))
if 's' in resp1.lower():#se a resposta for sim
    lista.append(resp2)#ela vai ser contabilizada
resp3 = str(input('MORA PERTO DA VÍTIMA? [S/N]: '))
if 's' in resp3.lower():
    lista.append(resp3)
resp4 = str(input('DEVIA PARA A VÍTIMA? [S/N]: '))
if 's' in resp4.lower():
    lista.append(resp4)
resp5 = str(input('JÁ TRABALHOU COM A VÍTIMA? [S/N]: '))
if 's' in resp5.lower():
    lista.append(resp5)
if len(lista) == 2:# se a lista tiver 2 elementos
    print('CLASSIFICAÇÃO = SUSPEITO')
elif (len(lista) >= 3) and (len(lista) <= 4): #se o número de elementos na lista for maior ou igual a 3 e menor ou igual a 4
    print('CLASSIFICAÇÃO = CÚMPLICE')
elif (len(lista) == 5): #se a lista tiver 5 elementos
    print('CLASSIFICAÇÃO = ASSASSINO')
else:
    print('CLASSIFICAÇÃO = INOCENTE')