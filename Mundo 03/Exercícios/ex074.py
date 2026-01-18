# gere 5 números aleatórios e bote-os em uma tupla
# mostre os números, o menor e o maior entre eles.
from random import randint

lista = []
for numero in range(5):
    lista.append(randint(0, 999))

tupla = tuple(lista)
print("Os numeros sorteados foram:")
for numero in tupla:
    print(f"{numero:^25}")
print(f"""O maior numero é {max(tupla)}.
O menor é {min(tupla)}.""")