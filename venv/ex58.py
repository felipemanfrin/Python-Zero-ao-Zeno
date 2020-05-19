import random
x = random.randint (0,10)
count = 1
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
palpite = int(input('Qual é seu palpite?  '))
while palpite != x :
    if palpite > x :
      palpite = int(input('Menos... Tente mais uma vez.  '))
    else :
        palpite = int(input('Mais... Tente mais uma vez.  '))
    count += 1
print('Acertou mizeravii! o numero que a maquina escolheu foi {} e você acertou em {} tentativas. Parabens!'.format(x,count))