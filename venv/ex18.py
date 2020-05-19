from math import radians, sin,cos,tan
ang = float(input('Digite o angulo desejado :  '))
print('Para o angulo {} , nos temos como sen {:.2f} , cos {:.2f}, e tg {:.2f}'.format(ang,sin(radians(ang)),cos(radians(ang)),tan(radians(ang))))