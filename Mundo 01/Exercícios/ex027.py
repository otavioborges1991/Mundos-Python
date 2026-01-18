# Faça um programa que leia um nome completo.
# Mostre o primeiro e último nomes separadamente.
import cores

nome_completo: str = " ".join(input('Digite um nome completo: ').strip().title().split())
nome_separado: list = nome_completo.split()
print(f'{cores.fverde}{nome_separado[0]}{cores.nenhum}, {cores.verde}{nome_separado[-1]}{cores.nenhum}.')


