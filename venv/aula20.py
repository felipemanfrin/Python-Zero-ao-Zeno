def soma (a,b):
    s = a + b
    print(s)

soma(4,5)
soma(2,1)
soma(1,4)

def contador (*num):
    tam = len(num)


contador(1,2,4,5,12,2,3)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [ 1, 2, 3, 4, 5]
dobra(valores)
print(valores)
