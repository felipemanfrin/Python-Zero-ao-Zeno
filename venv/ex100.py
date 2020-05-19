from time import sleep
from random import randint


def sorteia(lista):
    print('Sorteando 5 valores da lista : ', end='')
    for c in range (0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ',flush=True)
        sleep(0.3)


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando todos os valores pares de {lista}, temos {soma}')


numeros = list()
numeros1 = list()
sorteia(numeros)
somapar(numeros)

sorteia(numeros1)
somapar(numeros1)

