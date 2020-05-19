nome = str(input('digite uma frase:  ')).strip().upper()
print('Sua frase tem {} A`s nela'.format(nome.count('A')))
print('O primeiro A se encontra na posição {}'.format(nome.find('A')+1))
print('O ultimo A se encontra na posição {}'.format(nome.rfind('A')+1))