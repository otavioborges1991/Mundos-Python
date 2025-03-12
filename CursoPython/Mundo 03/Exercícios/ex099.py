# faça um programa com uma função chamada maior() que recebe vários números inteiros
# a função tem que dizer qual dos números é o maior
from random import randint

def maior(num):
    m = False
    for n in num:
        if n > m:
            m = n
    return m


valores = int(input("Quantos valores adicionar: "))
numeros = []
for n in range(valores):
    numeros.append(randint(1, 100))

print(numeros)
print(f'{maior(numeros)}')