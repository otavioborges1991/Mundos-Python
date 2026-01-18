# leia duas notas de aluna, calcule e mostre sua média
import cores
nota1 = float(input('Digite sua nota de matemática: '))
nota2 = float(input('Digite sua nota de ciência: '))
média = (nota1+nota2) / 2 # somar as notas primeiro devido à ordem de precedência de operações aritméticas.
print(f'Sua média é {cores.verde}{média:.1f}{cores.nenhum}.')