# largura = float(input('Digite a lagura (m): '))
# comprimento = float(input('Digite o comprimento (m): '))
# area = (largura * comprimento)
# print(area)

def area(larg,comp):
    a = larg * comp
    print(f'A area de um terreno de {larg} x {comp} é {a}')


l = float(input('Largura: '))
c = float(input('Comprimento: '))
area(l, c)

