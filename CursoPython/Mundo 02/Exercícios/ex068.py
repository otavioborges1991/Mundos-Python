# Jogue par ou impar com o computador.
# Termina quando o jogador perder e mostra quantas vitórias.
from random import randint

escolhas = ["Par", "Impar"]
vitorias = 0

while True:

    # essa parte do loop força o usuário a fazer uma escolha válida.
    escolha = str(input("Escolha par ou impar P/I: ")).strip().upper()
    if escolha == "P":
        jogador = escolhas[0] # escreve a escolha como Par
    elif escolha == 'I':
        jogador = escolhas[1] # escreve a escolha como Impar
    else:
        print('Escolha invalida')
        continue   # continue faz o loop recomeçar se a escolha for inválida.


    # Validando uma jogada.
    while True:
        jogada = int(input("Qual sua jogada entre 0 e 10: "))
        if 10 >= jogada >= 0 :
            break
        else:
            print("Jogada inválida.")

    computador = randint(1, 10)
    total = jogada + computador
    print(f"Computador jogou {computador} total {total}", "Par" if total %2 == 0 else "Impar")

    # detectando se jogando ganhou ou perdeu
    if total % 2 == 0:
        resultado = "Par"
    else:
        resultado = "Impar"
    if resultado != jogador:
        print("Perdeu!")
        break
    else:
        print("Ganhou! Vamos jogar novamente")
        vitorias += 1

print(f"GAME OVER! Você ganhou {vitorias} vez/vezes")
