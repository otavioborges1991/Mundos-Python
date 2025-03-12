# adapte o código do ex107 criando a função moeda() que mostre formatado, o valor monetário.

from utilidadesCeV import moeda

print("Manuseando moeda: ")
dinheiro = float(input("Quanto dinheiro: R$"))
aumentado = moeda.aumentar(dinheiro, 15)
diminuído = moeda.diminuir(dinheiro, 10)
dobrado = moeda.dobro(dinheiro)
metade = moeda.metade(dinheiro)

print(f'''
Valor Original: {dinheiro}

{'Ação':<15}{'Total':^10}

{'aumentado':.<15}{moeda.moeda(aumentado)}
{'diminuído':.<15}{moeda.moeda(diminuído)}
{'dobro':.<15}{moeda.moeda(dobrado)}
{'metade':.<15}{moeda.moeda(metade)}

''')