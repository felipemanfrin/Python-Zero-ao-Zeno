from datetime import datetime
lista = dict()
nome = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
carteira = int(input('Carteira de Trabalho (0 não tem): '))
idade = datetime.now().year - ano
if carteira == 0:
    lista = {'nome':nome,'idade':idade,'carteira':carteira}
else:
    contratacao = int(input('Ano de contratação: '))
    salario = int(input('Salário: R$ '))
    aposentadoria = (datetime.now().year - ano) + (35-(2020-contratacao))
    lista = {'nome':nome,'idade':idade,'carteira':carteira,'contratacao':contratacao,'salario':salario,'aposentadoria':aposentadoria}
for c,k in lista.items():
    print(f'{c} tem o valor {k}')
