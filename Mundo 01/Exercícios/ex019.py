# sorteie 1 de 4 nomes, leia o nome deles e escreva o escolhido.
import cores
from random import choice
print('Lendo nomes')
nome1 = input('Nome: ')
nome2 = input('Nome: ')
nome3 = input('Nome: ')
nome4 = input('Nome: ')
nomes = [nome1, nome2, nome3, nome4]
print(f'Os nomes são:{cores.fazul}{nomes}{cores.nenhum}')
escolhido = choice(nomes)
print(f'O escolhido foi {cores.fverde}{escolhido}{cores.nenhum}.')
