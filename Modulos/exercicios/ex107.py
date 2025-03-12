# crie um módulo chamado moeda.py que tenha as funções aumentar(algum %), diminuir(algum %)
# dobro() e metade()
# e também um programa que importe e use estes módulos e funções

from utilidadesCeV import moeda

print("Manuseando moeda:")
dinheiro = float(input("Quanto dinheiro: R$"))
aumentado = moeda.aumentar(dinheiro, 15)
diminuído = moeda.diminuir(dinheiro, 10)
dobrado = moeda.dobro(dinheiro)
metade = moeda.metade(dinheiro)

print(f'''
Valor Original: {dinheiro}

{'Ação':<15}{'Total':^10}
{'aumentado':.<15}R${aumentado:>8.2f}
{'diminuído':.<15}R${diminuído:>8.2f}
{'dobro':.<15}R${dobrado:>8.2f}
{'metade':.<15}R${metade:>8.2f}

''')