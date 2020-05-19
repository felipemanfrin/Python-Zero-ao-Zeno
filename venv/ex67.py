while True:
    n = int(input('Quer ver a tubuada de qual valor? '))
    tab = 1
    if n<0:
        break
    while tab < 11:
        tabuada = n * tab
        print(f'{n} x {tab} = {tabuada}')
        tab += 1
print('Tabuada encerrada')