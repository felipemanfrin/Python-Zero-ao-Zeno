nome = str(input('Digite seu nome completo :  ')).strip()
split = nome.split()
pnome = split[0]
tamanho = len(split)



print('o primeiro nome é {}, e seu ultimo nome é {}'.format(pnome,split[len(split)-1]))
print(tamanho)
