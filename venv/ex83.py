lista = list()
cont = cont1 = 0
ex = str(input('Digite a expressão: '))

for simb in ex:
    if simb == '(':
        cont+=1
    elif simb == ')':
        cont1+=1
if cont == cont1:
    print('Sua expressão é valida')
else:
    print('Sua expressão nao eh valida')
print(cont, cont1)
print(ex)

