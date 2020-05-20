def aumentar(p=0,n=0,format=False):
    if format == True:
        return f'{moeda(p * (1+(n/100)))}'
    return p * (1+(n/100))


def diminuir (p=0,n=0,format=False):
    if format == True:
        return f'{moeda(p * (1-(n/100)))}'
    return p * (1-(n/100))


def metade (p=0,format=False):
    if format == True:
        return f'{moeda(p/2)}'
    return p/2


def dobro (p=0, format=False):
    if format == True:
        return f'{moeda(p * 2)}'
    return p * 2


def moeda (p = 0, moeda = 'R$'):
    return f'{moeda}{p:.2f}'.replace('.',',')

