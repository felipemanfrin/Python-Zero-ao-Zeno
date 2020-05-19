p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA:  '))
c=0
while c != 10:
    c+=1
    p+= r
    print('{} - '.format(p),end='')
print('FIM')