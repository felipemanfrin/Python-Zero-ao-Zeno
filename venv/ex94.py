lista = list()
dic = dict()
soma = 0
while True:
    print(dic)
    nome = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if sexo in 'FM':
            break
    idade = int(input('Idade: '))
    dic = {'nome':nome,'sexo':sexo,'idade':idade}
    print(dic)
    lista.append(dic.copy())
    print(dic)
    while True :
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if cont in 'SN':
            break
    if cont == 'N':
        break
print(f'O grupo tem {len(lista)} pessoas')
for c in lista:
    soma += c['idade']
media = soma/len(lista)
print(f'A média de idade é de {media} anos ')
for c in lista:
    if c['sexo'] == 'F':
        print(f'{c["nome"]}',end=' ')
print('Lista das pessoas que estão acima da média: ')
for c in lista:
    if c['idade'] > media:
        for n,k in c.items():
            print(f'{n} = {k};', end=' ')
        print()
print('<< ENCERRADO >>')
