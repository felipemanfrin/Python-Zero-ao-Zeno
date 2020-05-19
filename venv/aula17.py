# nas listas nos usamos [] e nas tuplas nos usamos (). Nessa podemos adicionar novos produtos a esta lista diferente da tupla que eh imutavel

# lanche.append('biscoito') #adiciona o biscoito no final da lista
# # lanche.insert(0 , 'biscoito') #adiciona o biscoito na posição zero da lista
# # del lanche[3] # tira o terceirto intem da lista
# # lanche.pop(3) # tira o ultimo item da lista, mas nele vc pode passar o parametro msm assim que nem o del
# # lanche.remove('pizza')#tira em especifico os itens
# #
# # if 'pizza' in lanche:
# #     lanche.remove('pizza') #usamos esse comando para remover a pizza caso ela esteja na lista
# #
# # valores = list(range(4,11)) #vai criar uma lista de 4 ate 10 [4,5,6,7,8,9,10]
# # valores.sort()#coloca os numeros na ordem
# # valores.sort(reverse=True)
# # len(valore)# tamanho da lista

# num = [2,65,8,4,2,5]
# num[2] = 2
# num.append(7)
# num.sort(reverse=True)
# num.insert(4,6)
# num.pop(2)
# print(num)

valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor : ')))
# valores.append(1)
# valores.append(5)
# valores.append(8)
valores.sort()
for c , v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

a = [2,3,4,7]
b = a  # com esse comando voce conecta as duas listas
b[2] = 8
c = a[:] # ele esta copiando todos os valores de A como se fosse de 0 : ate o ultimo
print(f'Lista A: {a}')
print(f'Lista B: {b}')