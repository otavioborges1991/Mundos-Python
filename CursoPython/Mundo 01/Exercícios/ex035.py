# leia comprimento de 3 retas e diga se formão um triangulo
# o comprimento das 2 linhas menores tem que ser maior ou igual a maior linha para formar um triangulo
import cores
print("checando se o comprimento de 3 linhas formam um triangulo.")
linhas = [float(input("Lado 1: ")), float(input("Lado 1: ")), float(input("Lado 1: "))]

if sum(linhas) - max(linhas) > max(linhas):
    print(f'Essas linhas {cores.verde}formam{cores.nenhum} um triangulo.')
else:
    print(f'Essas linhas não {cores.vermelho}formam{cores.nenhum} um triangulo.')

