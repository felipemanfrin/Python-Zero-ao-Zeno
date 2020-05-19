n = int(input('Digite um número :  '))
div = 0
ndiv = 0
for c in range(1,n+1):
    if n%c == 0 :
        print('\033[34m{}'.format(c), end=' ')
    else:
        print('\033[33m{}'.format(c), end=' ')