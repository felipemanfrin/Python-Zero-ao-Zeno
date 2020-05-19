import math
print('Coloque os dois catetos da hipotenusa :  ')
a = float(input('a : '))
b = float(input('b = '))

c = (a**2 + b**2)
print(' A hipotenusa de {} e {} é {}'.format(a,b,math.sqrt(c)))