while True: #ENQUANTO FOR VERDADEIRO
    nome = str(input('NOME: '))
    salto = []
    count = 1
    soma = 0
    m = 0
    resp = ''

    for c in range(5): #para cada item em uma repetição de 5 vezes faça
        salto.append(float(input(f'SALTO {count}: '))) #adicione a lista de saltos o input
        count += 1 # some mais uma ao contador e mantenha o valor
        soma += salto[c]
        m = soma / 5
    print(f'Atleta: {nome}')
    print('--' * 20) #linha de separação multiplicada 30 vezes
    print(f'Primeiro salto: {salto[0]} m') #primeiro salto na posição 0
    print(f'Segundo salto: {salto[1]} m')
    print(f'Terceiro salto: {salto[2]} m')
    print(f'Quarto salto: {salto[3]} m')
    print(f'Quinto salto: {salto[4]} m')
    print('Resultado final: {:.2f} m'.format(m))

    resp = str(input('Deseja continuar [S/N]: '))

    if 'n' in resp.lower(): # SE CASO A RESPOSTA FOR NÃO
        break #PARE

print('ATLETAS CADASTRADOS COM SUCESSO')