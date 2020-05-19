p = int(input('Digite o primeiro numero de sua razão :  '))
n = int(input('Digite a razão da sua PA :  '))
decimo = p+(10-1)*n
for c in range (p,decimo+n,n) :
        print('{}'.format((c), end=' - '))