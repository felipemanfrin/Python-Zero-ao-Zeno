nome = str(input('Digite o nome da sua cidade:  '))
snome = nome.lstrip()
split = snome.split()
santos = 'santos' in split[0]
print('A primeira parte do nome de sua cidade começa com santos : {}'.format(santos))