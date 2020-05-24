try:
    a = int(input('denominador :'))
    b = int(input('numerador: '))
    r = b/a
except Exception as erro:
    print(f'Deu ruim menor {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('volte sempre')


x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")