# Usuário pode digitar 7 valores númericos.
# bote valores pares em uma lista, impares em outra.
# e as duas listas em uma outra lista que mantes separado os pares dos impares
# no final mostre os valores pares e impares em ordem crescente.

pares = []
impares = []
lista = [pares, impares]

for i in range(7):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

pares.sort()
impares.sort()
print(f"A lista complete contém os seguintes números: {lista}\nEstes são os pares {pares}\nE estes os impares {impares}.")

