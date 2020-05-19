n1 = float(input('Digite a nota de sua P1 :  '))
n2 = float(input('Digite a nota de sua P2 :  '))
media =(n1+n2)/2

if media<=5 :
    print('Voce esta reprovado!')
elif 5.0<media<6.9 :
    falta = 14-media
    print(' Você esta de recuperação e vai precisar de {} na sua P3 para passar'.format(falta))
elif media>=7:
    print('Você passou, parabens!')