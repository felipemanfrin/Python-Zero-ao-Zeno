frase = str(input('Digite uma frase:  ')).strip().upper()
separa = frase.split()
junto = ''.join(separa)
inverso =''
for c in range (len(junto)-1, -1 , -1):
    inverso+= junto[c]
if junto == inverso :
    print('Sua frase------ eh polidromica!')
else:
    print('Sua frase {} não é igual a {} ao contrario' .format(junto,inverso))