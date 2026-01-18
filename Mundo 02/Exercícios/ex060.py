# Leia um número e mostre o seu fatorial
# 5! = 5x4x3x2x1 = 120
from math import factorial

numero = int(input("Digite um  número: "))
contador = numero
fator = 1
# while loop para calcular fatorial o total é calculando dentro do loop
while contador > 0:
    # esses prints apenas escrevem a conta na tela.
    # eles não precisam existir para o fatorial estar certo.
    print(f'{contador}', end="")
    print(" x " if contador > 1 else " = ", end="")
    fator *= contador # esta linha e a abaixo que contam o fatorial.
    contador -= 1     # esta também controla o loop.
print(f'{fator}')
# O mesmo com for loop.
fator = 1 # zerando o resultado
for c in range(numero, 0,-1):
    print(f'{c}', end="")
    print(" x " if c > 1 else " = ", end="")
    fator *= c # esta linha conta o fatorial.
print(f'{fator}')


# usando a função factorial(num) ele retorna o fatorial de num
print(f'O fatorial de {numero} é {factorial(numero)}')