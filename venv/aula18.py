galera = list()
dado = list()
totalM = totalm = 0
for c in range(0,3):
    dado.append(str(input('Digite o nome: ')))
    dado.append(int(input('Idade: ')))
    print(dado)
    galera.append(dado[:])
    dado.clear()

for p in galera:
    print(p)
    if p[1]>=21:
        print(f'{p[0]} é maior de idade')
        totalM+=1
    else:
        print(f'{p[0]} é menor de idade')
        totalm+=1
print(f'{totalM} maiores de idade e {totalm} menores')
