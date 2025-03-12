# Leia nome e preço de vários produtos. Pergunte se é para continuar após cada um
# No final mostre:
# O total da compra.
# Quantos produtos custam mais de R$1000.
# O nome do produto mais barato.

total = 0
mais_de_miu = 0
mais_barato_nome = ""
mais_barato_preco = 0
print("Registrando compra de super mercado.")
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço R$"))
    total += preco

    if preco > 1000:
        mais_de_miu += 1

    if mais_barato_nome == "": # faz o primeiro produtor assumir o lugar do mais barato
        mais_barato_nome = produto
        mais_barato_preco = preco
    elif preco < mais_barato_preco: # depois somente produtos mais baratos entram no lugar dele.
        mais_barato_nome = produto
        mais_barato_preco = preco

    # perguntando se tem mais produtos.
    while True:
        continuar = str(input("Mais Produtos S/N: ")).strip().upper()[0]
        if continuar not in "SN":
            print("Escolha invalida.")
        else:
            break

    if continuar == "N":
        break

print(f"""
Total a pagar R${total:.2f}.
O produto mais barato foi {mais_barato_nome} custando R${mais_barato_preco}.
{mais_de_miu} produtos custando mais de R$1000 reais foram comprados.
""")