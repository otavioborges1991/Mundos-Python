# Programa gerencia o aproveitamento de um jogador de futebol.
# Leia nome do jogador e quantas partidas ele jogou. Depois quantos gols em cada partida
# Tudo guardado em um dicionário, incluindo total de gols feito durante o campeonato.

print("Gerenciando jogador de futebol")
nome = " ".join(str(input("Nome: ")).strip().title().split())
partidas = int(input("Em quantos jogos participou: "))
gols = []
for jogo in range(partidas):
    gols.append(int(input(f"Quantos Gol feito no jogo {jogo + 1}: ")))
jogador = {'nome': nome, 'partidas': partidas, 'gols': gols}

print()
print(jogador)
print(f'\nO jogador {jogador['nome']}, participou de {partidas} jogos.')
print("Nestes jogos ele marcou")
for partida, gols in enumerate(jogador['gols']):
    print(f"{gols} gols na partida {partida + 1}")