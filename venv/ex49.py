n = int(input('Escolha um valor entre 1 e 10 para ver sua tabuada :  '))
for x in range (1,11):
    resultado = n*x
    print('O resultado de {} x {} é {}'.format(n,x,resultado))