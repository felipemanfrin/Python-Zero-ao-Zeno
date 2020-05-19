peso = float(input('Digite o seu peso :  '))
altura = float(input('Digite sua altura :  '))

imc = peso/(altura*altura)

if imc<18.5 :
    print('Abaixo do peso')
elif 18.5<=imc<25 :
    print('Peso ideal')
elif 25<=imc<30 :
    print('Sobrepeso')
elif 30<=imc<40 :
    print('Obesidade')
elif imc>40 :
    print('Obesidade morbida')