import random
print('-'*25)
print('Digite : ')
print('1 - para pedra')
print('2 - para papel')
print('3 - para tesoura')
print('-'*25)
inp = int(input('Insira sua escolha :  '))
ia = random.randint(1,3)

if inp==1 and ia ==1:
    print('A IA jogou : {}'.format(ia))
    print('Empate')
elif inp==1 and ia==2 :
    print('A IA jogou : {}'.format(ia))
    print('IA ganhou')
elif inp==1 and ia==3 :
    print('A IA jogou : {}'.format(ia))
    print('Você ganhou!')
elif inp==2 and ia==2 :
    print('A IA jogou : {}'.format(ia))
    print('Empate')
elif inp==2 and ia ==3 :
    print('A IA jogou : {}'.format(ia))
    print('IA ganhou')
elif inp==2 and ia==1 :
    print('A IA jogou : {}'.format(ia))
    print('Voce ganhou!')
elif inp==3 and ia==3 :
    print('A IA jogou : {}'.format(ia))
    print('Empate')
elif inp==3 and ia==1 :
    print('A IA jogou : {}'.format(ia))
    print('Você ganhou!')
elif inp==3 and ia==2 :
    print('A IA jogou : {}'.format(ia))
    print('Você ganhou!')

