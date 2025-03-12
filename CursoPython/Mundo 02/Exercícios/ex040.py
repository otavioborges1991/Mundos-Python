# refazer exercicio 7 e adicione isto:
# abaixo de 5 reprovado, entre 5 e 6.9 recuperação, 7 ou mais, aprovado
import cores

nota1 = float(input('Digite sua nota de matemática: '))
nota2 = float(input('Digite sua nota de ciência: '))
média = (nota1+nota2) / 2 # somar as notas primeiro devido à ordem de precedência de operações aritméticas.
print(f'Sua média é {cores.verde}{média:.1f}{cores.nenhum}.')
if média < 5:
    print(f"{cores.vermelho}Reprovado!")
elif 5.9 >= média >= 5:
    print(f"{cores.amarelo}Recuperação!")
else:
    print(f"{cores.verde}Aprovado!")
