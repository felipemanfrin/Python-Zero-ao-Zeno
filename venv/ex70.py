total=caro=menorpreço=0
barato=''
while True:
    nome = str(input('Nome: '))
    preço = float(input('Preço: R$ '))
    total+=preço
    if preço> 1000:
        caro+=1
    if barato == '':
        barato = nome
        menorpreço = preço
    if barato != '':
        if preço<menorpreço:
            menorpreço = preço
            barato = nome
    continua = ' '
    while continua not in 'NS' :
        continua = str(input('Deseja continuar [S/N] ?')).upper().strip()[0]
    if continua == 'N':
        break
print(f'Temos {caro} a mais que 1000 o produto mais barato é {barato} e o preço total eh de {total}')
print('FIM')