# Leia 4 nomes e sorteie a ordem deles, então a.
from random import shuffle
import cores
print('Lendo nomes')
nome1 = input('Nome: ')
nome2 = input('Nome: ')
nome3 = input('Nome: ')
nome4 = input('Nome: ')
nomes = [nome1, nome2, nome3, nome4]
print(f'Os nomes são:{cores.verde}{nomes}{cores.nenhum}')
shuffle(nomes)
print(f're-ordenados fica {cores.fverde}{nomes}{cores.nenhum}.')

