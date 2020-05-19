# def leiaint(variavel):
#     variavel = (str(input(variavel)))
#     if variavel.isnumeric() :
#         variavel = int(variavel)
#     else:
#         print('ERRO! Digite um número inteiro válido')
#         variavel = print((str(input('Digite um numero: '))))
#     return variavel
#
#
#
# n = leiaint('Digite um n: ')
# print(f'Vc digitou {n}')
def LeiaInt(msg):
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = n
            ok = True
        else:
            print('\033[0;31m ERRO! Digite um numero.\033[m')
        if ok == True:
            break
    return valor


n = LeiaInt('Digite um número: ').strip()
print(f'Voce digitou {n}')