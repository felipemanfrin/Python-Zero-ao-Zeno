def escreva(txt):
    tamanho = len(txt)
    print('~' * tamanho)
    print(nome)
    print('~' * tamanho)


while True:
    nome = str(input('Digite nome: '))
    escreva(nome)
    while True:
        cont = str(input('Deseja inserir outro nome? [S/N] ')).upper().strip()
        if cont in 'NS' :
            break
    if cont == 'N':
        break