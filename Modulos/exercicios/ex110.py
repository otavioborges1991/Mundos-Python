# adicione ao modulo moeda.py a função resumo() que mostre na tela informações geradas pelas funções
# que ja temos no módulo criado até aqui

from utilidadesCeV import moeda

print("Manuseando moeda:")
dinheiro = float(input("Quanto dinheiro: R$"))
moeda.resumo(dinheiro, 20, 15)