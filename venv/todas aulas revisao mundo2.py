'''nome = str(input('Qual é seu nome :  '))
if nome == 'felipe':
    print('que nome bonito')
elif nome == 'vanessa' or nome == 'vanessinha':
    print('Voce esta pronta para ter um relacionamento gostoso com o felipe?')
else:
    print('que nome comum eim')
print('Tenha um bom dia {}'.format(nome))'''

"""print('Aprovar emprestimo :' )
vcasa = int(input('Digite o valor de sua casa: '))
salario = int(input('Digite quanto voce ganha de salario: '))
anos = int(input('Em quantos anos pretende pagar este emprestimo? '))
mensalidade = vcasa/(anos*12)
cota = salario*0.3
if mensalidade <= (cota):
    print('A mensalidade que voce terá que pagar por mes sera de {}'.format(mensalidade))
    print(cota)
else:
    print('O seu salario é muito baixo para conseguir este emprestimo')
"""

"""n = int(input('Digite um nuemro : '))
for c in range(0 ,n+1):
    print(c)
print('Esses foram os numeros pedidos')"""
'''import time
for c in range(10,-1,-1):
    time.sleep(1)
    print(c)
print('Feliz ano novo UHUUL')'''

'''for c in range(1,51):
    if c%2==0:
        print(c)'''

'''s=0
for c in range(3,500,3):
    if c%2==1:
        s+=c
        print(c)
print(s)'''

'''n = int(input('Digite um numero para saber sua tabuada: '))
for c in range (0,11):
    print('{}*{} = {}'.format(c,n,(c*n)))'''
'''s=0
for c in range(0,6):
    n = int(input('Digite seis numeros :  '))
    if n%2==0:
        s+=n
print(s)'''
'''s=0
pa = int(input('Digite a razão de sua PA: '))
for c in range(0,10):
    s+=pa
print(s)'''
'''s=0
n = int(input('Digite o valor de sua PA: '))
for c in range (0,10):
    s+=n
    print(s)'''

'''s=0
n = int(input('Digite um numero: '))
for c in range(2,n):
    if n%c==0:
      print('Este numero é primo')
    else:
        print('Numero nao primo')'''
'''inverso = ''
frase = str(input('Digite uma frase: ')).upper().split()
junto = ''.join(frase)
for c in range (len(junto)-1,-1,-1):
    inverso+=junto[c]
if junto==inverso:
    print('Sua palavrinha é palindromo')
else:
    print('Sua palavra {} é diferente de seu palindromo que é {}'.format(junto,inverso))'''
'''menor=0
maior=0
atual = 2020
for c in range (0,8):
    ano = int(input('Digite 7 anos de nascimento: '))
    if ano >= 2002:
        menor+=1
    else:
        maior+=1
print('Temos {} maiores de idade e {} menores de idade'.format(maior, menor))'''
'''mmaior=0
mediaidade=0
maisvelho=0
nomevelho= ''
for c in range (0,5):
    nome=str(input('Digite o nome: '))
    idade=int(input('DIgite a idade: '))
    sexo=str(input('Digite o sexo H ou  M: ')).upper()
    mediaidade+=idade
    if sexo=='M' and idade>=18:
        mmaior+=1
    elif sexo=='H' and idade>maisvelho:
        maisvelho=idade
        nomevelho=nome
print('Temos {} mulheres maiores de idade'.format(mmaior))
print('A media das idades é de {}'.format(mediaidade/5))
print('O homem mais velho é o {}'.format(nomevelho))
'''
'''sexo=''
sexo=str(input('Digite o sexo (F/M) :  ')).upper()
while sexo not in 'F/M':
    sexo=str(input('Digite o sexo (F/M) :  ')).upper()
print('voce eh {}'.format(sexo))'''

'''import random
z=1
x = int(input('Digite um numero de 0 a 10: '))
n = random.randint(0,10)
while x!= n:
    z+=1
    x = int(input('Digite um numero de 0 a 10: '))
print('Voce ACERTO MISERAVI , voce acertou em {} vezes.'.format(z))
'''
resultado = 0
n1 = int(input('Digite o primeiro numero : '))
n2 = int(input('Digite o segundo numero: '))
n3=0

while n3 != 5:
    print(''' 
[1]somar
[2]multiplicar
[3]maior
[4]novos numeros
[5]sair do programa
 ''')
'''    n3= int(input('Digite a opção desejada: '))
    if n3==1:
        resultado=n1+n2
        print('O resultado de sua soma é {}'.format(resultado))
    elif n3==2:
        resultado=n1*n2
        print('O resultado de sua multiplicação é {}'.format(resultado))
    elif n3==3:
        if n1>n2:
            resultado==n3
            print('O maior numero digitaro é o {}'.format(resultado))
        elif n1==n2:
            print('Seus numeros são de mesmo tamanho')
        else:
            resultado==n3
            print('O maior numero digitaro é o {}'.format(resultado))
    elif n3==4:
        n1 = int(input('Digite o primeiro numero : '))
        n2 = int(input('Digite o segundo numero: '))
    elif n3==5:
        print('FIM')'''

