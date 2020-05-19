aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] < 6:
    aluno['situacao'] = 'reprovado'
else:
    aluno['situacao'] = 'aprovado'
print(f'o {aluno["nome"]} com a media {aluno["media"]} foi {aluno["situacao"]} ')
for c, k in aluno.items():
    print(f'{c} : {k}')