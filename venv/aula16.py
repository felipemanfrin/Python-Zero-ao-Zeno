lanche = ('FELIPE' , 'VANESSA' , 'CYNTHIA')
'''for c in lanche:#c é uma variavel que armazena somente um valor e lanche eh uma tupla que armazena cada valor em um endereço
    print(f'Gosto muito da {c}')
# AS TUPLAS SAO IMUTAVEIS'''

#nome = str(input(' Digite seu nome completo: ')).strip()
nome = 'felipe', 'vanessa', 'cynthia'
for cont in range (0,len(nome)):
    print(nome[cont])
print(f'voce tem {nome} letras em seu nome')

'''for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')'''

'''print(sorted(lanche))
print(lanche)'''

'''a = (2,5,4)
b = (8,5,3,9)
c = a+b
print(c)
print(c.index(8))
print(c.count(5))'''