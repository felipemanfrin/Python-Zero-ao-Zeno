# mat = [[],[],[]]
# par = 0
# terceira = 0
# maior = 0
#
# for c in range (1,10):
#     valor = int(input('Digite um numero: '))
#     if valor % 2 == 0:
#        par += valor
#     if c <= 3:
#         mat[0].append(valor)
#     elif 3 < c <= 6 :
#         mat[1].append(valor)
#         if valor >= maior:
#             maior = valor
#     else:
#         mat[2].append(valor)
# terceira = (mat[0][2])+(mat[1][2])+(mat[2][2])
# print(mat[0])
# print(mat[1])
# print(mat[2])
# print(f"a soma de todos os pares é {par}")
# print(f'A soma da terceira coluna é {terceira}')
# print(f'O maior numero da seunda linha é {maior}')

matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = terceira = maior = 0
for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l} {c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if matriz[l][2]:
            terceira += matriz[l][2]
        if matriz[2][c]:
            if c == 0:
                maior = matriz[2][c]
            else:
                if matriz[2][c] > maior:
                    maior = matriz[2][c]
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}] ', end='')
    print()
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {terceira}')
print(f'O maior valor da segunda linha é {maior}')

