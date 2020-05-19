manipulador = open ('D://Downloads//texte.txt','w+')
manipulador.write('esse eh meu novo testinho/npulando a linha e bora ver ser pega mais de u ma linha')
manipulador.seek(0)
print('Metodo read():')
print(manipulador.read())

'''manipulador.seek(0) #volta para o começo da linha no arquivo, pois toda vez que ele lê o arquivo de testo ele marca com um ponteiro onde ele parou

print('Metodo readlines()')
print(manipulador.readline())
manipulador.seek(0)
mylines = manipulador.readline()
print(mylines)
for line in mylines:
 print(line.split())

manipulador.close()'''