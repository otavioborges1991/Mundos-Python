# calcule a soma entre todos os números impares que são múltiplos de 3 entre 1 e 500
import cores
soma = 0

print("Somando números impares entre 1 e 100 que são impar e divisivel por 3")
for numero in range(1, 500 + 1):
    print(f"Numero atual {cores.fazul}{cores.branco}{numero}{cores.nenhum}", end=" ")
    if numero % 2 == 1 and numero % 3 == 0:
        print(f"{cores.fverde}{cores.branco}é impar{cores.nenhum} e {cores.fverde}{cores.branco}divisível por 3{cores.nenhum}")
        soma += numero
    elif numero % 2 == 1:
        print(f"{cores.fverde}{cores.branco}É impar{cores.nenhum} mas {cores.fvermelho}{cores.branco}não é divisivel por 3{cores.nenhum}")
    elif numero % 3 == 0:
        print(f"{cores.fverde}{cores.branco}É divisível{cores.nenhum} por três mas {cores.fvermelho}{cores.branco}não é impar{cores.nenhum}")
    else:
        print(f"{cores.fvermelho}{cores.branco}não é impar{cores.nenhum}")
print(f"O total de numeros impares entre 1 e 500 é {soma}")
