# temp = list()
# lista = list()
# while True:
#     temp.append(str(input('Nome: ')))
#     temp.append(float(input('Nota 1: ')))
#     temp.append(float(input('Nota 2: ')))
#     lista.append(temp[:])
#     temp.clear()
#     cont = str(input('Quer continuar? [S/N] ')).upper().strip()
#     if cont == 'N':
#         break
# for c in range(0,len(lista)):
#     lista[c].append((lista[c][1] + lista[c][2])/2)
# print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
# print('-'*30)
# for c in range(0,len(lista)):
#     print(f'{c:<4}{lista[c][0]:<10}{lista[c][3]:>8.1f}')
# while True:
#     aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
#     if aluno == 999:
#         break
#     else:
#         print(f'Notas de {lista[aluno][0]} são {lista[aluno][1]} e {lista[aluno][2]}')

lista = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    lista.append([nome,[nota1,nota2],media])
    cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if cont == 'N':
        break
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for i, c in enumerate(lista):
    print(f'{i:<4}{c[0]:<10}{c[2]:>8}')
while True:
    num = int(input('Qual aluno gostaria de ver ? (999 intenrompe): '))
    if num == 999:
        break
    if num <= len(lista) - 1:
        print(f'As notas de {lista[num][0]} foram {lista[num][1]}')
print('FIM!')

