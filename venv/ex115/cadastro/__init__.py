cadastro = {'Ana Paula Vieira': '32 anos',
            'Claudio Mendonça':'18 anos',
            'Vanessa Matos':'23 anos',
            'Felipe Manfrin':'29 anos',
            'Renata Soares':'13 anos'}



def ListaPessoas(op = True):
    for c, k in cadastro.items():
        print(f'{c}  {k}')


def AdicionarLista(nome,idade):
    cadastro[nome] = idade