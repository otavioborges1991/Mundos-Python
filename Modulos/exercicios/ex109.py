# modifique as funções que foram criadas no ex107 com um parametro a mais
# que informe se o valor retornado por elas vai ser ou não formatado pela função moeda()
from utilidadesCeV import moeda

print("Manuseando moeda: ")
dinheiro = str(input("Quanto dinheiro: R$"))

print(f'''
Verificando se valores podem ser moedas
Valor Original: {dinheiro}

{'Ação':<15}{'Total':^10}

{'aumentado':.<15}{moeda.aumentar(dinheiro, 15, True)}
{'diminuído':.<15}{moeda.diminuir(dinheiro, 10, True)}
{'dobro':.<15}{moeda.dobro(dinheiro, True)}
{'metade':.<15}{moeda.metade(dinheiro, True)}

''')