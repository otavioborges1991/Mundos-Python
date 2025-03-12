# Faça um programa que tenha uma lista chamda números e duas funções chamadas sorteia() e somaPar()
# a primeira sortear-a 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
# entre todos os pares sorteados pela função anterior
from random import randint

def sorteia(total, menor, maior):
    lista = []
    for n in range(total):
        lista.append(randint(menor, maior))
    return lista

def soma_par(lista):
    total = 0
    for n in lista:
        if n % 2 == 0:
            total += n
    return total

números = sorteia(5, 0, 100)
pares = soma_par(números)

print(f'Os números sorteados foram: {números}. A soma dos pares nesta lista é = {pares}')
