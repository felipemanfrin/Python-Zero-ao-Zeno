from datetime import datetime
now = datetime.now()

ano = int(input('Digite o Ano em que voce nasceu :  '))
ali = now.year - ano

if ali>18 :
    falta = ali - 18
    print('Você já tem mais de 18 anos então provavelmente você já se alistou já faz {} anos'.format(falta))
elif ali==18 :
    print('Voce deve se alistar esse ano ! não falte!')
else:
    falta = 18 - ali
    print('Você ainda não tem 18 anos, daqui {} anos você devera se alistar'.format(falta))
