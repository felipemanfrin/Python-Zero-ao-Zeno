from ex111a2.utilidadesCeV import moeda
from ex111a2.utilidadesCeV import dados

p = dados.validacao('Digite o preço: R$')
moeda.resumo(p, 50, 50)