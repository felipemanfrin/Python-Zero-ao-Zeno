salario = float(input('escreva seu salario: '))
if salario<=1250:
    aumento = salario*1.15
    print('Seu salario com o aumento de 15% é {}'.format(aumento))
else:
    aumento = salario*1.10
    print('Seu salario com o aumento de 10% é {}'.format(aumento))