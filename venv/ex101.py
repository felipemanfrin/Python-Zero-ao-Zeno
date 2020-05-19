def voto(ano):
    """
    ->Essa função é para descobrir se a pessoa devera votar oou não
    :param ano: ano que a pessoa nasceu
    :return: retorna a string sobre a obrigatoriedade do voto do cidadão
    """
    from datetime import date
    hoje = date.today().year
    if (hoje-ano) >= 18 and (hoje - ano) <65:
        return 'obrigatorio'
    elif (hoje - ano) < 18:
        return 'negado'
    else:
        return 'opcional'


idade = int(input('Digite seu ano de nascimento: '))
print(f'O seu voto é {voto(idade)}')

