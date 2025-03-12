# Leia vários números e coloque-os em uma lista
# Crias 2 listas extras e conterão somente valores pares e impares.
# Mostre as 3 listas.

lista = []
pares = []
impares = []
while True:

    resposta = str(input("Quer digitar um número? S/N: ")).strip().upper()[0]
    if resposta == "S":
        pass
    elif resposta == "N":
        break
    else:
        print("Resposta invalida. Escreva S ou N para sim ou não.")
        continue

    número = int(input("Digite um número: "))
    lista.append(número)

    if número % 2 == 0:
        pares.append(número)
    else:
        impares.append(número)

print(f'a lista {lista} contem estes pares {pares} e estes impares {impares}')