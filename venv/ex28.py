import random
numb=random.randint(0,5)
#print(numb)
n1 = int(input(' Digite um numero de 0 a 5:  '))
if n1==numb:
    print('VOCE acertou o numero que o pc chutou')
else:
    print('o Numero que a maquina chutou foi {}. Tente novamente'.format(numb))