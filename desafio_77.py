pal = ('APRENDER',
       'PROGRAMAR',
       'LINGUAGEM',
       'PHYTON',
       'CURSO',
       'GRATIS',
       'ESTUDAR',
       'PRATICAR',
       'TRABALHAR',
       'MERCADO',
       'PROGRAMADOR',
       'FUTURO')
for p in pal:
    print('\nNa palavra {} temos'.format(p), end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')
