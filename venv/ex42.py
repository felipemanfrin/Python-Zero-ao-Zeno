l1 = int(input('Digite o tamanho do primeiro lado :  '))
l2 = int(input('Digite o tamanho do segundo lado :  '))
l3 = int(input('DIgite o tamanho do terceiro lado :  '))

s1=l1+l2
s2=l2+l3
s3=l1+l3

if (s1 or s2 or s3) < (l1 or l2 or l3):
    print('Não é um triângulo')
elif l1==l2==l3:
    print('O triangulo é equilareto')
elif l1==l2 or l2==l3 or l1==l3 :
    print('O triangilo é isoceles')
elif l1!=l2!=l3!=l1 :
    print('O triangulo é escaleno')
