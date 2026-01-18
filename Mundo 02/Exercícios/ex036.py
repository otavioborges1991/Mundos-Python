# Programa para aprovar impréstimo para a compra de uma casa.
# Pergunte: valor da casa, o salário do comprador e em quantos anos ira pagar.
# Calcule o valor da prestação mensal, não pode exceder 30% do salário ou então o
# impréstimo será negado.
import cores

print("Aprovação de impréstimo.")
casa = float(input("Valor da casa: R$"))
salário = float(input("Valor do seu salário: R$"))
anos = int(input("Quantos anos para pagar: "))
parcela =  casa / (anos * 12)
credito = salário * (30/100)
print(f'''
Parcela mensal R${parcela:.2f}.
Seu credito é R${credito:.2f}.''')

if credito >= parcela:
    print(f"Impréstimo {cores.verde}aprovado{cores.nenhum}.")
else:
    print(f"Impréstimo {cores.vermelho}rejeitado{cores.nenhum}.")
