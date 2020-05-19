'''import math
n = int(input('Digite um numero para calcular seu fatorial :  '))
f = math.factorial(n)
print('O fatorial é {}'.format(f))'''
n = int(input('Digite um numero para saber seu fatorial: '))
fat=1
for c in range (1,n+1):
    fat*=c
print('Seu fatorial é {}'.format(fat))