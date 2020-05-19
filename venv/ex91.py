# from random import randint
# from time import sleep
# lista = dict()
# grupo = list()
# for c in range (0,4):
#     jogador = randint (1,10)
#     lista = {'jogador':jogador}
#     grupo.append(lista.copy())
# print(grupo)
# count = 1
# for c in grupo:
#     print(f'Jogador{count} : {c["jogador"]}  ')
#     sleep(1)
#
#     count += 1

from operator import itemgetter
from random import randint
from time import sleep

jogador = { 'jogador 1' : randint(0,10),
            'jogador 2' : randint(0,10),
            'jogador 3' : randint(0,10),
            'jogador 4' : randint(0,10)
}
rank = list()
for c,k in jogador.items():
    print(f'{c} tirou {k}')
    sleep(1)
rank = sorted(jogador.items(), key=itemgetter(1),reverse=True)
print(rank)
print('-='*30)
for c,k in enumerate(rank):
    print(f'{c+1} Colocado é o {k[0]}')
    sleep(1)





