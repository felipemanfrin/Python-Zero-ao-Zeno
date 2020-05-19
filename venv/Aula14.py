n = 1
impar = par = 0
while n != 0:
    n = int(input('Digite um numero :'))
    if n % 2 == 0 :
        par += 1
    else:
        impar += 1
print('Voce digitou {} numeros pares e {} numeros impares'.format(par,impar))
print('Acabou')