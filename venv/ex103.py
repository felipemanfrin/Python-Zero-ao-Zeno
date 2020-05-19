def ficha(nome = '<Desconhecido>', gols = 0):
    print(f'O jogador {nome} fez {gols} no campeonato')
    print(type(gols))


n = str(input('Nome: '))
g = str(input('Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)


