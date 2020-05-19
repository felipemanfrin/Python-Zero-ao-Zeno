np = list()
maisp = list()
menosp = list()
temp = list()
co = 0
while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(int(input('Peso: ')))
    np.append(temp[:])
    print(temp)
    temp.clear()
    print(np)
    outro = str(input('Deseja continuar [S/N]?' )).upper().strip()
    while outro not in 'NS':
        outro = str(input('[S/N] PARA CONTINUAR: ')).upper().strip()
    if outro == 'N':
        break
# if co == 0:
#     maisp.append(temp)
#     menosp.append(temp)
    # print(menosp,maisp)
# else:
for p in np:
    if co == 0:
        maisp.append(np[0])
        menosp.append(np[0])
    else:
        if p[1] > maisp[0][1]:
            maisp.clear()
            maisp.append(p[:])
        elif p[1] < menosp [0][1]:
            menosp.clear()
            menosp.append(p[:])
    co += 1
print(f'A lista de nome tem {len(np)}')
print(f'O menor peso {menosp}, e o maior peso {maisp}')

