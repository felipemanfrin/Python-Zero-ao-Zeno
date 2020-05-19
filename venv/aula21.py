# def contador(i, f, p):
#     """
#     Isso se chama 'DOCSTRING'
#     -> Faz uma contagem e mostra na tela
#     :param i: Inicio da contagem
#     :param f: Fim da contagem
#     :param p: Passo de contagem
#     :return: Não possui retorno
#     """
#     c = i
#     while c<f:
#         print(f'{c}', end=' ')
#         c += p
#
#
# contador(0,10,2)
#
# #parametros Opcionais
#
# def somar(a=0, b=0, c=0):
#     s = a+b+c
#     print(f'A soma é de {s}')
#
#
# somar(1,2,3)
# somar(1,2)# mesmo sem 3 parametros ele funciona, pois dei para o parametro um valor opncional

#scopos global e local
# def teste(b):
#     global a
#     a = 8
#     b += 4
#     c = 2
#     print(f'a dentro vale {a}')
#     print(f'b dentro vale {b}')
#     print(f'c dentro vale {c}')
#
#
# a = 5
# teste(a)
# print(f'a global vale {a}')
#
#
#
# #retornando valores
# def somar (a=0, b=0, c=0):
#     s =a+b+c
#     return s
#
#
# resp = somar(1,2,3) # voce manda para somar os parametros e como no fim ele retorna de volta voce tem que ter uma variavel para receber esses parametros
# r1 = somar(1,2,3)
# r2 = somar(2,65,7)
# r3 = somar(4,5,7)
# print(f'Meus calculos deram {r1} {r2} {r3}')


def par(num = 1):
    if num % 2 == 0:
        return True
    else:
        return False


n = int(input('Digite um numero: '))
print(par(n))