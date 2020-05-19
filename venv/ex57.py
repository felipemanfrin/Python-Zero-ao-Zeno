sexo = str(input(' Digite o seu  sexo [M/F]')).strip().upper()
while sexo not in 'MF' :
    sexo = str(input('Digite o sexo com os caracteres corretos [M/F]:  '))
print('O seu sexo é {} '.format(sexo))
