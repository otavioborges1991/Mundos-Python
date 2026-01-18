# jogo de adivinhação, um numero entre 0 e 5 é gerado
# usuário tem que adivinhar o numero escolhido
# se o usuário acertar. uma mensagem mostre que ele
# ganhou, se não, uma menssagem diz que ele perdeu.
from random import randint
import cores

número = randint(0,5)
print("Jogo da adivinhação.")
escolha = int(input('Adivinhe um numero entre 0 e 5: '))
if número == escolha:
    print('Acertou!')
else:
    print(f'Errou, o número era {cores.verde}{número}{cores.nenhum}.')