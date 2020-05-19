numero = int(input('Digite um numero qualquer ou 999 para seu encerramento:  '))
soma=0
count=0
while numero != 999:
    soma += numero
    count+=1
    numero = int(input('Digite um numero qualquer ou 999 para seu encerramento:  '))
print('A soma de todos os numeros é de {} e voce escolheu {} numeros: '.format(soma,count))