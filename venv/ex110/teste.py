def metade(p=0, format=False):
    if format == True:
        return moeda(p/2)
    else:
        return p / 2


def dobro(p=0, n=0, format=False):
    if format == True:
        return moeda(p*2)
    else:
        return p * 2


def aumento(p=0, n=0, format=False):
    if format == True:
        return moeda(p*(1+(n/100)))
    else:
        return p*(1+(n/100))


def diminui(p=0, n=0, format=False):
    if format == True:
        return moeda(p*(1-(n/100)))
    else:
        return p*(1-(n/100))


def moeda (p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'


def resumo (p=0,aum=10,red=10):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado:  \t{p}')
    print(f'Dobro do preço:  \t{dobro(p,True)}')
    print(f'Metade do preço:  \t{metade(p,True)}')
    print(f'{aum}% de aumento:  \t{aumento(p,aum,True)}')
    print(f'{red}% de redução:  \t{diminui(p,red,True)}')


