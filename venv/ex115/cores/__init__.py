def pintarLetra(numero,conteudo):
    if numero == 0:
        #amarelo
        return f'\033[0;33m{conteudo}\033[0;0m'
    if numero == 1:
        #azul
        return f'\033[34m{conteudo}\033[0;0m'


def Estilo(msg):
    print('-'*30)
    print(f'{msg}'.center(30))
    print('-'*30)


def Estilo2(msg):
    print('-' * 30)
    print(f'{msg}')



