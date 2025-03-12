# Leia 5 valores numéricos e bote-os numa lista
# Mostre o maior, o menor e suas respectivas posições

lista = [] # inicializando uma lista
# preenchendo a lista
for numero in range(5):
    lista.append(int(input("Digite um número: ")))

# descobrindo o maior número listado.
maior = max(lista)
maiorpos = []
# gravando posição dos números idênticos ao maior.
if lista.count(maior) > 1:
    for indice, numero in enumerate(lista):
        if numero == maior:
            maiorpos.append(indice)
else:
    maiorpos = lista.index(maior)

# descobrindo o menor número
menor = min(lista)
menorpos = []
# gravando posição dos números idênticos ao menor.
if lista.count(menor) > 1:
    for indice, numero in enumerate(lista):
        if numero == menor:
            menorpos.append(indice)
else:
    menorpos = lista.index(menor)

print(f'Na lista de números: {lista}, o maior número é o {maior}, na posição {maiorpos}º, e o menor é {menor}, na posição {menorpos}º.')
