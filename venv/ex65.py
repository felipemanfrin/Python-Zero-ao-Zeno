resp = 'S'
total=cont=num=maior=menor=0
while resp in 'Ss':
    nun = int(input('Digite um numero : '))
    cont+=1
    total+=(nun)
    if cont == 1:
        maior = menor = nun
    else:
        if nun>maior:
            maior=nun
        elif num<menor:
            menor=nun
    resp = str(input('Quer continuar (S/N) ')).upper().strip()[0]
print('A media será {} , o maior numero é {} e o menor numero é {} '.format((total/cont),maior,menor))