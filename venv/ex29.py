v = int(input('velocidade do carro:  '))
multa = (80-v)*7
if v<=80:
    print('Voce esta na velocidade certa parabens')
else:
    print('Voce esta acima da velocidade e vai pagar uma multa de R${}'.format(multa*-1))