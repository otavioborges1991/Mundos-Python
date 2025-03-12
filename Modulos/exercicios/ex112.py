# crie função leia_dinheiro() no módulo dado em utilidadesCev, que funcione como input()
# mas com validação de dados para aceitar apenas valores monetários, incluindo com virgula.

from utilidadesCeV import dado
from utilidadesCeV.dado import leia_dinheiro

valor = leia_dinheiro('Digite um valor: ')
print(valor)