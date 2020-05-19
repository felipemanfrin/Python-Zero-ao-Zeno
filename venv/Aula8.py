import math
num = int(input('Digite um numero para saber sua raiz:  '))
raiz= math.sqrt(num)
print('A Raiz de {}  é igual a {:.2f} '.format(num,math.ceil(raiz)))