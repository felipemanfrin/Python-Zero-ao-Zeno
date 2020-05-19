print('-'*30)
print('Calculadora de água diaria')
print('-'*30)
while True:
    nome = str(input('Entre com seu nome: '))
    peso = float(input('Peso : '))
    aguatotal = peso*35
    copos = aguatotal/200
    print(f'Já que seu peso é de {peso} você deveria beber {aguatotal} ml de agua por dia, equivalente a {copos:.{0}f} copos de agua . ')
    print('-' * 30)
    novo = str(input('Você deseja inserrir novo peso [S/N]? ')).upper().strip()[0]
    print('-' * 30)
    while novo not in 'SN':
        novo = str(input('Você deseja inserrir novo peso [S/N]? ')).upper().strip()[0]
    if novo == 'N':
        print('Obrigado pelo sua atenção ^_^')
        break
print('-'*30)