count = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'deis', 'onze', 'doze', 'treze', 'quatorze',
         'quinze', 'dezesseis', 'dezesete', 'dezoito',
         'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20: '))
while True:
    if num >= 0 <= 20:
        break
    num = int(input('ERRO! digite um número entre 0 e 20: '))
print(count[num])







