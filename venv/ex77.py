tupla = ('felipe','se','importa','muito','com','a','vanessa','e','queria','ela','bem','e','feliz')
x=0
for c in tupla:
    print(f'\n A palavra {c} tem as seguintes vogais ',end='')
    for letra in c:
        if letra in 'aeiou':
            print(letra, end=' ')
