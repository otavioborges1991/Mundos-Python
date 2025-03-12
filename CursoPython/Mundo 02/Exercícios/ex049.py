# refazer o ex009, tabuada. usando for loops.
import cores

print("Fazendo a tabuada.")
numero = int(input("digite um número: "))
for i in range(1, 11):
    print(f'{cores.azul}{numero}{cores.nenhum} x {cores.amarelo}{i}{cores.nenhum} = {cores.verde}{numero*i}{cores.nenhum}')

