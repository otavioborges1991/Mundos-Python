# 4 jogadores jogam um dado com resultados aleátorios
# guarde os resultados num dicionário. No final, coloque o dicionário em ordem
# sabendo que o vencedor tirou o maior número no dado.
from random import randint
from operator import itemgetter # itemgetter para encontrar o valor que eu quero para o sorted()
from time import sleep


jogadores = {"jogador1": randint(1, 20),
             "jogador2": randint(1, 20),
             "jogador3": randint(1, 20),
             "jogador4": randint(1, 20)}

for jogador, dado in jogadores.items():
    print(f'O {jogador} tirou {dado} no dado')
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('\nRanqueados ficam')
for rank, jogador in enumerate(ranking):
    print(f'{rank +1 }º lugar: {jogador[0]} tirou {jogador[1]} no dado')
    sleep(1)