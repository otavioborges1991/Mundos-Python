# crie um pacote chamado utilidadesCeV que tenha dois módulo internos
# chamados moeda e dado, transfira as funções ultilizados nos ex107 ao ex110
# para o primeiro pacote e mantenha tudo funcionando

from utilidadesCeV import moeda

print("Manuseando moeda:")
dinheiro = float(input("Quanto dinheiro: R$"))
moeda.resumo(dinheiro, 20, 15)