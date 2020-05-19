menor = 0
maior = 0
for p in range(1 , 6):
    peso = float(input('Peso da {} pessoa:  '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso é {}'.format(menor))
print('o maior peso é {}'.format(maior))
