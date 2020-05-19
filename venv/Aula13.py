#n1 = int(input('Digite o valor do seu salario'))
#print(''' Digite sua forma de pagamento
#[1] A vista
#[2]cartão
#[3]cheque''')
#pagamento = int(input(':'))

#if pagamento == 1 or 2 or 3:
#    if pagamento == 1:
#        print('pagou a vista {}'.format(n1))
#    elif pagamento == 2:
#        print('pagamento cartao {}'.format(n1))
#    else:
#        print('pagamento cheque {}'.format(n1))
s = 0
for c in range(0,3):
    n = int(input('Digite um valor :  '))
    s +=n
print('A soma de todos os valores foi {} '.format(s))