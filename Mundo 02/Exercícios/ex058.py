# Melhores o ex028
# Escolher um número entre 0 e 10, jogador pode tentar adivinhar até acertar.
# Mostre quantos erros quando acertar.

from random import randint
import cores

número = randint(0,10)
tentativa = 0
print("Jogo da adivinhação.")
while True:
    escolha = int(input('Adivinhe um numero entre 0 e 10: '))
    tentativa += 1
    if escolha > número:
        print(f'{cores.vermelho}Errou{cores.nenhum}.')
        print("Menos... tente de novo")
    elif escolha < número:
        print(f'{cores.vermelho}Errou{cores.nenhum}.')
        print("Mais... tente de novo")
    else:
        print(f"{cores.verde}Acertou{cores.nenhum}, o número era {cores.verde}{número}{cores.nenhum}")
        break

print(f"{cores.famarelo}{cores.branco} {tentativa} {cores.nenhum} tentativas.")