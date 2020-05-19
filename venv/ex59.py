n1 = int(input(' Digite o primeiro digito:  '))
n2 = int(input('Digite o segundo digito:  '))
escolha = 0
while escolha != 5:
    print('''      [1] somar
      [2] multiplicar
      [3] maior
      [4] novos numeros
      [5] sair do programa''')
    escolha = int(input('>>>>>>>>>>Qual opção :'))
    if escolha == 1:
        soma = n1+n2
        print('A soma entre {} + {} = {} '.format(n1,n2,soma))
    elif escolha == 3 :
        if n1>n2:
            maior = n1
        else:
            maior = n2
    elif escolha == 4 :
        n1 = int(input('Digite o primeiro numero:  '))
        n2 = int(input('Digite o segundo numero:  '))
    elif escolha == 2 :
        mult = n1*n2
        print('A mult entre {} * {} = {} '.format(n1,n2,mult))
    elif escolha == 5 :
        print('fim')
    else :
        print('Opção invalida. Tente novamente ')
