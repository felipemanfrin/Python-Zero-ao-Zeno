#\033[0;30;41m

#primeiro numero é para estilo
#segundo para cor das letras
#terceiro para cor de funto

#0 == none
#1 == bold
#4 == underline
#7 == negative(ao contrario)

#0 branco
#1 vermelho
#2 verde
#3 amarelo
#4 azul
#5 roxo
#6 azul clarim
#7 cinza

#print('\033[1;31;43mOlá mundo!')
#não deixar a faixinha ate o fim
#print('\033[1;31;43mOlá mundo!\033[m')
F = 'Felipe'
V = 'Vanessa'
print('O nome meu nome é \033[35m{}\033[m e da pessoa que eu namoro é \033[33m{}\033[m'.format(F,V))
print('Oi Muit prazer em te conhecer {}{}{}!!!!'.format('\033[4;34m',F,'\033[m'))
