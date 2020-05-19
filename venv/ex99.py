# lista = list()
# def maior(lst):
#     ultimo = len(lst)
#     plus = 0
#     for k, c in enumerate(lst):
#         print(c)
#         plus += 1
#     print(f'O maior numero é {lst[plus - 1]}')
#
#
# while True:
#     n = int(input('Numero: '))
#     lista.append(n)
#     cont = str(input('Continue? ')).upper()
#     while cont not in 'SN':
#         print('Erro!')
#         cont = str(input('Continue? ')).upper()
#     if cont == 'N':
#         break
# maior(sorted(lista))

def maior(*num):
    maior = cont = 0
    print('-='*30)
    print('\nOs valores analizados são : ', end=' ')
    for valor in num:
        print(f'{valor}',end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor é de {maior}')



maior(2,3,45,6,76,1,3)
maior(1,2,5,6,1,5)
maior(1)
maior()
