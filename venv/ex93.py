# lista = dict()
# gols = list()
# total = 0
# nome = str(input('Nome do jogador: '))
# partidas = int(input(f'Quantas partidas {nome} jogou? '))
# for c in range (1,partidas+1):
#     pontos = int(input(f'Quantos gols na partida {c}? '))
#     total += pontos
#     gols.append(pontos)
# lista = {'nome':nome,'gols':gols,'total':total}
# print('-='*30)
# print(lista)
# print('-='*30)
# for c,n in lista.items():
#     print(f'O campo {c} tem o valor {n}')
# print('-='*30)
# print(f'O jogador {nome} jogou {partidas}.')
# for c,n in enumerate(gols):
#     print(f' na partida {c+1}, fez {n} gols.')

score = dict()
gols = list()
score['nome'] = str(input('Nome: '))
partidas = int(input(f'Quantas partidas {score["nome"]} jogou? '))
for c in range (0,partidas):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
score['gols'] = gols[:]
score['total'] = sum(gols)
for c ,n in score.items():
    print(f'O campo {c} tem o valor {n}')
print('-='*20)
print(f'O jogador {score["nome"]} jogou {partidas} partidas')
for c in range (0, partidas):
    print(f'Na partida {c+1}, fez {gols[c]}')