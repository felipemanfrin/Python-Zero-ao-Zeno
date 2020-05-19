num = int(input('Digite um numero entre 1 e 9999:  '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('Milhar: {}'.format(m))