# def notas(*n, situacao = False):
#     """
#     -> Pega as notas de varios alunos e tira sua media
#     :param n: nota dos alunos analizados
#     :param situacao: relacionado a media das notas
#     :return: retorna um dicionario com a media, maior , menor e total de notas, e a situaçao
#     """
#     total = media = 0
#     for e, v in enumerate(n):
#         total += 1
#         media += v
#         if e == 0:
#             menor = v
#             maior = v
#         else:
#             if v > maior:
#                 maior = v
#             elif v < menor:
#                 menor = v
#     if situacao :
#         if media < 6:
#             situacao = 'RUIM'
#         elif 6 <= media < 8:
#             situacao = 'Razoável'
#         else:
#             situacao = 'OTIMA'
#     dic['media'] = media/total
#     dic['maior'] = maior
#     dic['menor'] = menor
#     dic['total'] = total
#     dic['situação'] = situacao
#     return dic



def notas(*n, situacao=False):
    dic = dict()
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['media'] = sum(n)/len(n)
    if dic :
        if dic['media'] < 6:
            dic['situacao'] = 'Ruim'
        elif 6 <= dic['media'] < 8:
            dic['situacao'] = 'razoavel'
        else :
            dic['situacao'] = 'Otima!'
    return dic


resp = notas(5.5, 9.5, 10, 6.5)
print(resp)
