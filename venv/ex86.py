# matriz = [[],[],[]]
# for p in range (1,10):
#     valor = int(input('Digite o valor '))
#     if p <= 3 :
#         matriz[0].append(valor)
#     elif 3 < p <= 6:
#         matriz[1].append(valor)
#     else:
#         matriz[2].append(valor)
# print(f'\n {matriz[0]} \n {matriz[1]} \n {matriz[2]}')
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite o numero para posição {l} {c} '))
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()