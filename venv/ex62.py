p = int(input('Digite o primeiro termo de sua PA: '))
r = int(input('Digite a razão da PA: '))
c=0
while c <10:
    c+=1
    p=p+r
    print(p)
    if c==10:
        novo = int(input('Mais quantos termos voce deseja de sua PA :'))
        pa = c+novo
        while novo != 0:
            while c < pa :
                c+=1
                p=p+r
                print(p)
                if c==pa:
                    novo = int(input('Deseja mais quantos termos do PAA?  '))
                    pa=c+novo

        print('valeu irmao')



