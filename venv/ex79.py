conjunto = list()
continuar = ''
while True:
    numero = (int(input('Digite um numero: ')))
    if numero not in conjunto:
        conjunto.append(numero)
    else:
        print('oi bebezinho  podi não')
    continuar = str(input('Deseja continuar [S/N]')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]')).upper().strip()
    if continuar == 'N':
        break
print(sorted(conjunto))
