pro = ('Lápis', 1.75,
       'Borracha', 2.00,
       'Caderno', 15.90,
       'Estojo', 25.00,
       'Transferidor', 4.20,
       'Compasso', 9.99,
       'Mochila', 120.32,
       'Canetas', 22.30,
       'Livros', 34.90)
print('='*30)
print('LISTA DE PREÇOS')
for po in range(0, len(pro)):
    if po % 2 == 0:
        print(pro[po], end=' ')
    else:
        print(pro[po])


