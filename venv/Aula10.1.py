#tempo=int(input('Quantos anos tem seu carro?  '))
#if tempo<=3:
#    print('carro novo')
#else:
#     print('carro velho')

# ou pode ser print('carro novo 'if tempo <=3 else 'carro velho')
n1 = float(input('Digite a nota da sua P1:  '))
n2 = float(input('Digite a nota da sua P2:  '))
n3 = (n1+n2)/2

if n3>=6 :
    print('Sua nota final é {:.1f} , e você passou de ano'.format(n3))
else:
    print('Sua nota final é {:.1f} , e voce precisa fazer prova final'.format(n3))