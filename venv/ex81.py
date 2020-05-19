numeros = list()
while True:
    numeros.append(int(input('Digite um numero: ')))
    continuar = str(input('Deseja continuar? ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Digite [S/N] como opção')).strip().upper()[0]
    if continuar in 'N':
        break
if 5 in numeros:
    print('Temos numeros 5 na lista')
else:
    print('Nao temos o 5 na lista')
print(f'Temos {len(numeros)} numeros digitados')
numeros.sort(reverse=True)
print(f'A lista em ordem decrescente é {numeros}')

