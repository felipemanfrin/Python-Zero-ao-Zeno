v = 0
menor =0
maior =0
todos = 0
for pessoa in range(0, 7, 1):
    v = int(input('Em que ano a {} pessoa nasceu?  '.format(pessoa+1)))
    if v<2011 :
        maior+=1
    else:
        menor+=1
print('{} São maiores de idade'.format(maior))
print('{} São menores de idade'.format(menor))