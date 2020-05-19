# from time import sleep
#
#
# def contador (inicio, fim, passo):
#     if passo == 0:
#         passo = 1
#     elif passo < 0:
#         passo = passo*(-1)
#     for c in range (1, 11):
#         print(c , end=' ')
#         # sleep(1)
#         if c == 10 :
#             print()
#             for c in range (10, 0, -1):
#                 print(c, end=' ')
#                 # sleep(1)
#     if fim > inicio:
#         print()
#         for c in range (inicio, fim+1, passo):
#             print(c, end=' ')
#     else:
#         print()
#         if fim <= 0:
#             fim -= 1
#         elif fim > 0:
#             fim += 1
#
#         for c in range (inicio, fim, - passo):
#             print(c, end=' ')
#
#
# i = int(input('Inicio: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
#
# contador(i,f,p)

from time import sleep

def contador(inicio,fim,passo):
    if passo < 0:
        passo *= (-1)
    elif passo == 0:
        passo = 1
    print('-='*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    cont = inicio
    if inicio < fim:
        while cont <= fim:
            print(f'{cont}',end=' ')
            cont += passo
        print('\nFIM!')
    else:
        while cont >= fim:
            print(f'{cont}',end=' ')
            cont -= passo
        print('\nFIM!')


contador(0,10,1)
contador(10,0,2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)