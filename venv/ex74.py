# import random
# x=['','','','','']
# maior=menor=0
# for i in range(0,5):
#     w = random.randint(1,10)
#     x[i]=w
#     if i==0:
#         maior=menor=w
#     if maior<w:
#         maior=w
#     if menor>w:
#         menor=w
# print(f'Os valores sorteados são {x}')
# print(f'o maior valor sorteado foi {maior}')
# print(f'O menor valor sorteado foi {menor}')

from random import randint
n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'Os valores sorteados são : {n} ')
print(f'O maior numero dos sorteados é {max(n)}')
print(f'O menor numero dos sorteados é {min(n)}')

