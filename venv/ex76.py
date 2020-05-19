x = tuple
c = ''
while True:
    nome=str(input('Digite o nome do produto: '))
    valor=float(input('Digite o valor do produto:  '))
    for c in range (1,):
        x[c] = nome
        x[c+1] = valor
        continue1=str(input('Voce quer continuar[s/n]? ')).upper().strip()
    if continue1 == 'SN':
        break
print(x)