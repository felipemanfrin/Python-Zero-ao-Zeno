# x=['','','','']
# # y=['','','','']
# # count=count3=count9=posisao=posisao2=0
# # for c in range (0,4):
# #     count+=1
# #     numero=int(input(f'Digite o {count} numero.  '))
# #     x[c] = numero
# #     posisao+=1
# #     if numero == 9:
# #         count9+=1
# #     if x[c] == 3 and count3<1:
# #         count3+=1
# #         posisao2 = posisao
# #     if numero%2==0:
# #         y[c]=numero
# #     if posisao2==0:
# #         posisao2 = 'Nem foi digitado'
# # print(f'Temos o numero 9 {count9} vezes, o primeiro numero 3 esta na posição {posisao2}, e {x} ')
# # print(f' O primeiro 3 esta na {x.index(3)+1} posicão')
num = (int(input('Digite o 1 numero : ')),int(input('Digite o 2 numero : ')),int(input('Digite o 3 numero : ')),int(input('Digite o 4 numero : ')))
print(f'Temos {num.count(9)} novez ' )
if num==3:
    print(f'O valor 3 apareceu na {num.index(3)+1} posição')
else:
    print('Nao tiveram nenhum 3')
print('Os valores pares são :',end=' ')
for n in num:
    if n%2==0:
        print(n ,end=' ')



