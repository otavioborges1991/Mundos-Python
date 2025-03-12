# jogue pedra, papel e tesoura, contra a maquina
import cores
from random import choice
from caixastr import caixa

escolhas = ['Pedra', 'Papel', 'Tesoura']
caixa("Jogo de Jokenpo.")
# este código vai dar erro se jogador escolher qualquer número fora do índice de 0 a 2.
jogador = escolhas[int(input('''Faça sua escolha!
| 0 = Pedra | 1 = Papel | 2 = Tesoura |
Escolha: '''))]
computador = choice(escolhas)
print(f'''
Você:{cores.fazul}{cores.branco}{jogador}{cores.nenhum}
Computador:{cores.fmagenta}{cores.branco}{computador}{cores.nenhum}
Resultado:''', end=" ")
if computador == jogador:
    print(f'{cores.azul}Empate!{cores.nenhum}')
elif (computador == escolhas[0] and jogador == escolhas[2]
      or computador == escolhas[1] and jogador == escolhas[0]
      or computador == escolhas[2] and jogador == escolhas[1]):
    print(f'{cores.fvermelho}{cores.branco}Derrota!{cores.nenhum}')
else:
    print(f'{cores.fverde}{cores.branco}Vitória!{cores.nenhum}')

