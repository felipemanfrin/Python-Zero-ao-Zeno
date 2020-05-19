# dados = dict()
# locadora = list()
# locadora2 = list()
# dados = {'nome':'Pedro','idade':25}
# print(dados['nome'])
# print(dados['idade'])
# filme = {
#     'titulo':'star wars',
#     'ano':'1977',
#     'diretor':'George Lucas'
# }
#
# filme2 = {
#     'titulo':'star wars2',
#     'ano':'1978',
#     'diretor':'George Lucass'
# }
# print(filme)
# print(filme.values())#vai retornar todos os valores do dicionario
# print(filme.keys())#ele vai retornar as chaves 'titulos do endereço'
# print(filme.items())#ele vai pegar os dois
#
# for k,v in filme.items():
#     print(f'o {k} é {v}')
#
# locadora2.append(filme)
# locadora.append(locadora2[:])
# locadora2.clear()
# locadora2.append(filme2)
# locadora.append(locadora2[:])
# print(locadora)
# print(locadora[0][0]['ano'])
#
# pessoas = () tupla
# pessoas = [] lista
# pessoas = {} dicionario

pessoas = {'nome':'Felipe','idade':'29','sexo':'M'}
pessoas['nome'] = 'vanessa'#troca o nome
for k, v in pessoas.items():
    print(f'{k} {v}')

estado = dict()
brasil = list()
for c in range (0,2):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
print(brasil[0]['sigla'])
for c in brasil:
    for k, v in c.items():
        print(f'{k} {v}')