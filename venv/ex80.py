conjunto = list()
# continuar = ''
# while True:
#     numero = (int(input('Digite um numero: ')))
#     if numero not in conjunto:
#         conjunto.append(numero)
#     else:
#         print('oi bebezinho  podi não')
#     continuar = str(input('Deseja continuar [S/N]')).upper().strip()
#     for n in range(0,len(conjunto)):
#         if n>(n+1):
#             temp = n
#             n = (n+1)
#              = temp
#     while continuar not in 'SN':
#         continuar = str(input('Deseja continuar [S/N]')).upper().strip()
#     if continuar == 'N':
#         break
# print(sorted(conjunto))
for c in range (0,5):
    numero = int(input('Digite um valor: '))
    if c == 0 or numero > conjunto[-1]:
        conjunto.append(numero)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(conjunto):
            if numero <= conjunto[pos]:
                conjunto.insert(pos, numero)
                break
            pos += 1
print(conjunto)

