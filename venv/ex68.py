import random
PI=''
c=0
while True:
    n = int(input('Digite um numero: '))
    escolha = str(input('Par ou Impar[P/I]')).upper().strip()[0]
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar[P/I]')).upper().strip()[0]
    ai = random.randint(0,10)
    soma=n+ai
    if soma%2==0:
        PI='P'
    if soma%2==1:
        PI='I'
    if PI!=escolha:
        break
    c += 1
    print(f'Voce digitou {n} e o computador digitou {ai}. Total de {soma} deu {PI} ')
print(f'Voce digitou {n} e o computador digitou {ai}. Total de {soma} deu {PI} e ganhou {c} vezes')
print('Voce perdeu')