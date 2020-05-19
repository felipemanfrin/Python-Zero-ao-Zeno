km = float(input('Digite a distancia em km percorrida: '))
if km<=200 :
    taxa = km*0.50
    print('a preço da sua viagem será {}'.format(taxa))
else:
    taxa = km*0.45
    print('O valor da passagem é {}'.format(taxa))