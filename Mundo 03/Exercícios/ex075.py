# leia 4 valores e guarde-os em uma tupla
# Mostre quantos números 9 nela.
# Em que posição esta o primeiro número 3.
# Quais foram os números pares.

lista = []
pares = []
print("Adicionando números a uma lista")
for n in range(4):
    lista.append(int(input("Digite um número: ")))
    if lista[n] % 2 == 0:
        pares.append(lista[n])

tupla = tuple(lista)
print(f"na tupla tem {tupla.count(9)} números 9, o primeiro número 3 esta no índice {tupla.index(3)}")
print(f"os pares foram {pares}")

