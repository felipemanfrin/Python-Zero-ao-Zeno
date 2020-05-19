def linhazinha (linha):
    print('~' * (len(linha)+3))
    print(f'{linha}')
    print('~' * (len(linha)+3))


print(linhazinha('SISTEMA DE AJUDA PyHELP'))
while True:
    comando = str(input('Função ou Biblioteca > '))
    linhazinha(f'Acessando o manual do comando "{comando}" ' )
    if comando.lower() == 'fim':
        break
    else:
        help(comando)
print(linhazinha('Ate logo!'))

