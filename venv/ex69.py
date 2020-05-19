'''cmulher=chomem=cidade=0
while True:
    idade=int(input('Digite a idade da pessoa: '))
    sexo=str(input('Digite o sexo da pessoa[H/M]: ')).upper().strip()[0]
    while sexo not in 'HM':
        sexo = str(input('Digite o sexo da pessoa[F/M]: ')).upper().strip()[0]
    if sexo=='H':
        chomem+=1
    if sexo=='M' and idade>=18:
        cmulher+=1
    if idade>=18:
        cidade+=1
    novo = str(input('Quer inserir outra pessoa[S/N]?')).upper().strip()[0]
    while novo not in 'SN':
        novo=str(input('Quer inserir outra pessoa[S/N]?')).upper().strip()[0]
    if novo!='S':
        break
print(f'Temos {cidade} pessoas maiores de idade , {chomem} homens cadastrados, e {cmulher} mulheres com mais de 20 anos ')
'''
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M]')).upper().strip()[0]
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'{idade} {sexo}')
