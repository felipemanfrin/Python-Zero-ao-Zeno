somaidade = 0
mediaidade = 0
hidadeidoso = 0
hnome = ''
qmulheres = 0

for p in range (1,5):
    print('{} PESSOA'.format(p))
    nome = str(input('Nome:  ')).strip()
    idade = int(input('Idade:  '))
    sexo = str(input('Sexo [M/F]:  ')).strip()
    somaidade += idade
    if sexo in 'Mm' and p==1 :
        hnome = nome
        hidadeidoso = idade
    if hidadeidoso<idade and sexo in 'Mm':
        hidadeidoso = idade
        hnome = nome
    if sexo in 'Ff' and idade>=20:
        qmulheres+=1
mediaidade = somaidade/4
print('A media das idades é {}'.format(mediaidade))
print('O nome do mais velho é {} e sua idade é de {} '.format(hnome,hidadeidoso))
print('Temos {} mulheres com idade maior que 20 '.format(qmulheres))