preco = float(input('Insira o valor do produto a ser pago :  '))
print('''Escolha o metodo de pagamento:
 [1] A vista ou cheque
 [2] a vista cartão
 [3] 2x no cartao
 [4] 3x ou mais no cartão''')
opcao = int(input('Digite a opção :  '))

if opcao == 1 :
    final = preco*0.90
    print('O valor a se pagar nesses metodos é de {} '.format(final))
elif opcao == 2 :
    final = preco*0.95
    print('O valor a se pagar é de {}'.format(final))
elif opcao == 3 :
    final = preco
    print('o valor a se pagar é de {} '.format(final))
else :
    final = preco *1.20
    print('O valor a se pagar é de {} '.format(final))
