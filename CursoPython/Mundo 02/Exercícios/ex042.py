# refazer o 35 e adicione isto:
# mostre que tipo de triângulo é criado
# equilateral, todos os lados igual
# isosceles, dois lados iguais
# escaleno, todos os lados diferentes

import cores
print("checando se o comprimento de 3 linhas formam um triângulo.")
linhas = [float(input("Lado 1: ")), float(input("Lado 1: ")), float(input("Lado 1: "))]
tipo = "nenhum"
triângulo = False                           # não é registrado um triângulo até fazer o teste, abaixo
if sum(linhas) - max(linhas) > max(linhas): # se as três linhas formam um triângulo
    triângulo = True                        # se registra um triângulo
if triângulo:
    if linhas[0] == linhas[1] == linhas[2]: # todos os lados iguais
        tipo = "equilateral"
    elif linhas[0] == linhas[1] or linhas[0] == linhas[2] or linhas[1] == linhas[2] : # dois lados iguais
        tipo = "isosceles"
    else: # nenhum lado igual
        tipo = "escaleno"

if triângulo:
    print(f'Essas linhas {cores.verde}formam{cores.nenhum} um triângulo do tipo {cores.magenta}{tipo}{cores.nenhum}.')
else:
    print(f'Essas linhas {cores.vermelho}não formam{cores.nenhum} um triângulo.')

