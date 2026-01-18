# aprimore o ex086 mostrando no final
# a soma de todos os pares
# a soma dos valores da terceira coluna
# o maior valor da segundo linha


matriz = [[], [], []]
pares = 0
soma_coluna3 = 0
maior_linha2 = 0
numero_mais_longo = 0

for linha in range(3):
    for coluna in range(3):
        numero = int(input(f"Digite um número para linha {linha} coluna {coluna}:"))
        if len(str(numero)) >= numero_mais_longo:
            numero_mais_longo = len(str(numero))
        matriz[linha].append(numero)



for linha in matriz:
    for numero in linha:
        print(f'|{numero:^{numero_mais_longo}}', end="") # formatando dinamicamente, de acordo com
    print("|")                                           # o numero mais longo na matriz.

for linha in matriz:
    for coluna, numero in enumerate(linha):
        if numero % 2 == 0:
            pares += numero
        if coluna == 2:
            soma_coluna3 += numero
maior_linha2 = max(matriz[1])

print(f"{pares} Foram os pares digitados na matriz.\n"
      f"{soma_coluna3} é a soma da coluna 3.\n"
      f"{maior_linha2} é o maior da linha 2.")

