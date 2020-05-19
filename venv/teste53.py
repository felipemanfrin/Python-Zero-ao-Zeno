frase = str(input('Digite uma frase :  ')).upper().strip()
separa = frase.split()
junta = ''.join(separa)
inverso = ''
for letra in range (len(junta)-1,-1,-1):
    inverso += junta[letra]
print(inverso,letra)