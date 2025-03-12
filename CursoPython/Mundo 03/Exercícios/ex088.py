# crie palpites para mega sena, o programa pergunta quantos jogos para sortear
# 6 números entre 1 e 60 para cada jogo cadastrando todos em uma lista composta
# não pode haver números repetidos dentro de um mesmo jogo.
from random import randint


jogos = 0
palpites = list()

print("Gerando jogos de mega sena")
while True:
    jogos = int(input("Quantos jogos jogar: "))
    for jogo in range(jogos):
        palpites.clear()
        # gerando jogos
        while True: # loop infinito checa por números repetidos. não são permitidos.
            numero = randint(1, 60)
            if numero not in palpites:
                palpites.append(numero)
            if len(palpites) >= 6:
                break
        print(f'{palpites}')


    # zerando resposta
    continuar = "0"
    # perguntando se quer continuar a criar jogos
    while continuar not in "SN":
        continuar = str(input("Continuar a jogar S/N: ")).strip().upper()[0]
        if continuar not in 'SN':
            print("Resposta invalida.")
    # sai do loop se a resposta for não
    if continuar == "N":
        break

