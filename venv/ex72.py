# numero = int(input('Digite um numero entre 0 e 20: '))
# contagem = 'zero','um','dois', 'tres','quatro','cinco', 'seis', 'sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte'
# while numero >20 or numero < 0:
#     numero = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
# for n in range (0,len(contagem)):
#     if n == numero  :
#         print(f'Voce digitou o numero {contagem[n]} {n}')

contagem = 'zero','um','dois', 'tres','quatro','cinco', 'seis', 'sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte'

while True:
    numero = int(input('Digite um numero entre 0 e 20 : '))
    if 0<= numero <=20:
        break
    print('Tente novamente. ', end='')
print(f'O numero que voce digitou foi {contagem[numero]}.')
while True:
    novo = str(input('Quer digitar outro numero [S/N]? ')).upper().strip()[0]
    if novo in 'S':
     numero=int(input('Digite um numero entre 0 e 20 : '))
     print(f'O sumero que voce digitou foi {contagem[numero]}')
    else:
        break
print('Volte sempre! ')
