max=min=maxpos=minpos=0
listamin = list()
listamax = list()
lista = list()
for c in range (0,5):
    numeros = int(input(f'Digite o {c+1} numero : '))
    lista.append(numeros)
    if c == 0 :
        min=max=numeros
    else:
        if numeros >= max:
            max = numeros
            listamax.append(c)
            # maxpos = c
        if numeros <= min:
            min = numeros
            listamin.append(c)
            # minpos = c
print(f'O maior valor foi {max}, e sua posição {listamax}')
print(f'O menor valor foi {min}, e sua posicão {listamin}')
