'''print('= '*30)
print('{:^30}:'.format('BANCO DO FELIPE'))
print('='*30)
valor = int(input('Valor a ser sacado: '))
total = valor
ced50=ced20=ced1=ced10=0
while True:
    while total-50>=0:
        ced50+=1
        total-=50
    while total-50<0 and total-20>=0:
        ced20+=1
        total-=20
    while total-20<0 and total-10>=0:
        ced10+=1
        total-=10
    while total-10<0 and total-1>=0:
        ced1+=1
        total-=1
    if total-1<=0:
        break
print(f'50:{ced50}, 20:{ced20}, 10:{ced10}, 1:{ced1}')'''

print('='*30)
print('{:^30}'.format('BANCO COMUNISTA'))
print('='*30)
valor = int(input('Que valor quer sacar? R$'))
total=valor
ced=50
totalced=0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        print(f'Total de {totalced} cedulas de R${ced}  ')
        if ced == 50:
            ced = 20
        if ced == 20:
            ced = 10
        if ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break



