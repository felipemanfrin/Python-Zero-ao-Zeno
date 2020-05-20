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


def resumo (p,aum,red):
    print('-'*30)
    print('RESUMO DO VALOR')
    print('-'*30)
    print(f'Preço analisado:  {p}')
    print(f'Dobro do preço:  {dobro(p,True)}')
    print(f'Metade do preço:  {metade(p,True)}')
    print(f'{aum}% de aumento:  {aumento(p,aum,True)}')
    print(f'{red}% de redução:  {diminui(p,red,True)}')


