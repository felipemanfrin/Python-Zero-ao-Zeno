times = ('keyd1','flamengo2','prodigy3','pain4','furia5','intz6','redemption7','kabum8','tsm9','c910','skt11','fanatic12','dignitas13')
x=0
# for T in times:
#
#     if x<5:
#         print(f'Os top 5 times são {x+1} é o {times[x]}')
#        # print(f'os ultimo quatro colocados são {times[13:8:-1]}')
#     x += 1
#     if x<5:
#         print(f'os 4 ultimos colocados são {times[-x]}')
# print(f'A lista dos times é {times}')
# print(f'Os primeiros 5 times são {times[0:5]}')
# print(f'os ultimo 4 times são {times[13:8:-1]}')
# print(f' A Kabum esta na {times.find(kabum8)} posição')
# for t in times:
#     print(t)
print(f'Os ultimos quatro colocados são {times[-4:]}')
print('-='*15)
print(f'Os cinco primeiros colocados são {times[:5]}')
print('-='*15)
print(f'A pain esta na {times.index("pain4")+1} posição')