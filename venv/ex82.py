lista1 = list()
lista2 = list()
lista3 = list()

while True:
    numero = int(input('Digite um numero: '))
    lista1.append(numero)
    continuar = str(input('Deseja continuar [S/N] ? ')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Digite [S/N] :  ')).upper().strip()
    # if numero%2 == 0:
    #     lista2.append(numero)
    # if numero%2 == 1:
    #     lista3.append(numero)
    if continuar in 'N':
        break
for c in lista1:
    if c % 2 == 0:
        lista2.append(c)
    if c % 2 == 1:
        lista3.append(c)
print(f'A lista inteira é {lista1}')
print(f'A lista de numeros parares {lista2}')
print(f'A lista de numeros impares {lista3}')

