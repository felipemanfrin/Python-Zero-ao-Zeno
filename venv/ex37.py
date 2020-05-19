import struct
num = int(input('Digite um numero inteiro : '))
print('-'*40)
print('''Escolha uma das bases para conversão :
[1]Para converção binária')
[2]Para conveção octal')
[3]Para converção hexadecimal''')
print('-'*40)
opcao = int(input('Digite sua opção :  '))
if opcao == 1 :
    print('{} convertido para binario é igual a {}'.format(num,bin(num)))
elif opcao == 2 :
    print('{} convertido para octal é igual a {}'.format(num, oct(num)))
elif opcao ==3 :
    print('{} convertido para hexadecimal é igual a {}'.format(num,dec(num)))