# Aprimore o ex093, para que ele funcione com vários jogadores, incluindo um sistema de
# Visualização de detalhes de aproveitamento de cada jogador.

jogadores = []
print("Gerenciando jogador de futebol")
while True:
    # Perguntando se quer adicionar mais um jogador
    resposta = str(input("Quer adicionar um jogador S/N: ")).strip().upper()[0]
    if resposta not in "SN":
        print("Resposta invalida, digite apenas S para sim ou N para não.")
        continue
    elif resposta in "N":
        break

    nome = " ".join(str(input("Nome: ")).strip().title().split())
    partidas = int(input("Em quantos jogos participou: "))
    gols = []
    for jogo in range(partidas):
        gols.append(int(input(f"Quantos Gol feito no jogo {jogo + 1}: ")))
    jogador = {'nome': nome, 'partidas': partidas, 'gols': gols}
    jogadores.append(jogador)

if len(jogadores) == 0:
    exit("Nenhuma jogador adicionado")

print("\nLista de jogadores")
print(f"{"ID":>3} {'Jogador':<40}{'Partidas'} {'Gols por partida'}")
for ID, jogador in enumerate(jogadores):
    print(f'{ID:>3} {jogador["nome"]:.<40}{jogador["partidas"]:^8}', end=" ")
    for jogo in range(jogador['partidas']):
        print(f"{jogador['gols'][jogo]}", end=" ")
    print()


print("Analisando jogador")
while True:
    # Perguntando se quer analisar um jogador
    resposta = str(input("Quer analisar um jogador S/N: ")).strip().upper()[0]
    if resposta not in "SN":
        print("Resposta invalida, digite apenas S para sim ou N para não.")
        continue
    elif resposta in "N":
        break

    while True:
        ID = int(input("Digite o ID do jogador a analisar: "))
        if ID > len(jogadores) or ID < 0:
            print("Jogador invalido")
            continue
        else:
            break

    for chave, valor in jogadores[ID].items():
        print(f'{chave}: {valor}')

