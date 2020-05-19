from time import sleep
lista = list()
jog = dict()
gols = list()
gtemp = list()
contador = total = 0
while True:
    nome = str(input('Nome: '))
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    for c in range (0,partidas):
        g = int(input(f'Quantos gols na partida {c+1}? '))
        gtemp.append(g)
    gols.append(gtemp[:])
    total = sum(gtemp)
    gtemp.clear()
    jog = {'nome':nome,'partidas':partidas,'gols':gols[contador],'total': total}
    lista.append(jog.copy())
    contador += 1
    cont = str(input('Quer continuar? [N/S] ')).upper().strip()[0]
    if cont == 'N':
        break
print('-='*30)
print(f'{"Cod.":<1} {"NOME":<10} {"gols":<15} {"total":>8}')
for n,c in enumerate(lista):
    print(f'{n}     {c["nome"]}        {c["gols"]}           {c["total"]}', end='')
    print()
while True:
    consulta = int(input('Mostrar dados de qual jogador? '))
    if consulta in range (0,len(lista)):
        print(f'LEVANTAMENTO DO JOGADOR {lista[consulta]["nome"]}')
        for n,c in enumerate(lista[consulta]['gols']):
            print(f'No jogo {n+1} fez {c}. ')
            sleep(1)
    elif consulta == 999:
        break
    else:
        print(f'ERRO! Não existe jogador com código {consulta}! Tente novamente ')

