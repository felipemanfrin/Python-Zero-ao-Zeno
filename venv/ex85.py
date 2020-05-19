tot = [[], []]
for c in range(0,7):
    nun = int(input(f'Digite o {c+1}. valor: '))
    if nun % 2 == 0:
        tot[0].append(nun)
    else:
        tot[1].append(nun)

print(tot[0],tot[1],tot)
