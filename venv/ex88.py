import random
from time import sleep
lista = list()
jogos = list()
c = 0
quantos = int(input('Quantos jogs você quer : '))
while c < quantos:
    while True:
        num = random.randint(0, 60)
        if num not in lista:
            lista.append(num)
        if len(lista) == 6:
            break
    jogos.append(sorted(lista[:]))
    lista.clear()
    c += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1} : {l}')
    sleep(1)
print('Boa sorte!!!')



