from ex115.cores import pintarLetra
from ex115.cores import Estilo,Estilo2
from ex115.cadastro import ListaPessoas,AdicionarLista


Estilo('MENU PRINCIPAL')

while True:
    print(f'{pintarLetra(0,1)} - {pintarLetra(1,"Ver pessoas cadastradas")}\n'
    f'{pintarLetra(0,2)} - {pintarLetra(1,"Cadastrar nova pessoa")}\n'
    f'{pintarLetra(0,3)} - {pintarLetra(1,"Sair do sistema")} ')
    n = int(input(Estilo2(pintarLetra(0,'Sua Opção: '))))
    if n == 1:
        print(ListaPessoas())
    elif n == 2:
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        AdicionarLista(nome,f'{idade} anos')
    elif n == 3:
        break
    else:
        print(f'Numero não esperado por motivo de \n')


