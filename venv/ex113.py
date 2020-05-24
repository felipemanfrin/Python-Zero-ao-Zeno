def LeiaInt(msg):
    """
    Nesta função consegue entregar um numero inteiro , e caso contrario aponta o erro encontrado
    :param msg: é o texto mostrado para o usuario
    :return: retorna o valor inteiro apos ser verificado
    """
    while True:
        try:
            n = int(input(msg))
        # except (TypeError, ValueError):
        #     print(f'Tipo errado! ')
        except Exception as erro:
            print(f'O problema encontrado foi {erro.__class__}')
        else:
            break
    return n


def LeiaFloat(msg):
    while True:
        try:
            c = float(input(msg))
        except Exception as erro:
            print(f'O erro encontrado foia {erro.__class__}')
        except KeyboardInterrupt:
            return c==0
        else:
            break
    return c



n = LeiaInt('Digite um número: ')
c = LeiaFloat('Digite um númeroa: ')
print(f'O valor inteiro é {n} e o real é {c}')
