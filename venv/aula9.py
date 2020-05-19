#Fatiamento de frase, frase[9:21] - vai de 0 ate a letra 20.
# frase [:5] - vai do zero ate o 4.
# frase[15:] - vai da 15 ate o ultimo caractere.
# frase[9::3] - vai começar no 9 e vai ate o final e pula de 3 em 3
#len(frase) - mostra o tamanho da string.
# frase.count('o') - vai contar quantas vezes tem a letra 'o'.
# frase.count( 'o',0,13) - procura letras 'o' do zero ate o 12.
# frase.find('deo') -  vai indicar onde ele começa a frase 'deo' na string.
# 'curso' in frase - se tiver a palavra curso dentro da lista frase ele devolve true.
# frasse.replace( 'python', 'android') -  ele substitui a palavra python por android.
# frase.upper() - ele coloca todas as letras para maiusculo .
# frase.lower() - coloca todas as letras para minusculo.
# frase.capitalize() -  todos os caracteres ficam tudo minusculo e a primeira letra fica maiuscula.
# frase.title() -  ele vai capitalizar todas as primeira letra de toda palavra depois dos espaços.
# frase.strip() -  ele tira todos os espaços no começo e no fim da string.
# frase.lstrip() ou frase.rstrip() - tira os espaços da direita ou esquerda.
# frase.split() - divide sua string nos espaços em uma lista com todas essas palavras em novas strings ou inves de uma string só.
# '-'.join(frase) - ele coloca o caractere entre as aspas nos espaços.

frase = 'felipe é gostoseaum'
print(len(frase))
dividido = frase.split()
print(dividido[0][3])
print(len(dividido))
teste = ''.join(dividido)
print(len(teste))
print(frase[:5])