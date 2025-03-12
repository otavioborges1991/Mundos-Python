# cria uma matriz 3x3 e preencha com valores lidos pelo teclado
# mostre a matriz formatado com as colunas e linhas 0, 1 e 2.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # matriz com 3 linhas
# matrix = [[], [], []]

for linha in range(3):
    for coluna in range(3):
        numero = int(input(f"Digite um número para linha {linha} coluna {coluna}:"))
        matriz[linha][coluna] = (numero)
        # matriz[linha].append(numero)


print(13*'-')
for linha in matriz:
    for numero in linha:
        print(f'|{numero:^3}', end="")
    print("|")
print(13*'-')

