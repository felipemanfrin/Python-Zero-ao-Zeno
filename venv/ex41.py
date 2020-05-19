from datetime import datetime
now = datetime.now()
ano = int(input('Digite o seu ano de nascimento :  '))
atual = now.year - ano

if atual<=9 :
    print('vc é da categoria mirim')
elif 9<atual<=14 :
    print('Você é da catergoria infantil')
elif 14<atual<=19 :
    print('Você é da categoria junior')
elif 19<atual<=20 :
    print('Você é da categoria senior')
elif atual>20 :
    print('voce é da categoria MASTER')