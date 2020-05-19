def fatorial(num, conta = False):
    """
    -> calcula o fatorial de um numero
    :param num: Numero a ser calculado
    :param conta: Se mostrará a conta ou não
    :return: retorna o resultado fatorial total
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if conta:
            print(f'{c} x ', end= ' ')
    return f


print(fatorial(5,False))

