# leia 3 números, mostre o maior e o menor.
import cores

num = [input("Digite um número: "), input("Digite um número: "), input("Digite um número: ")]
# resolvendo o problema usando funções do python
maior = max(num)
menor = min(num)
print(f'O maior valor é {cores.vermelho}{maior}{cores.nenhum}, e o menor é {cores.azul}{menor}{cores.nenhum} usando max() e min()')
# usando if
maior = num[0]
menor = num[0]
if num[1] < num[0] and num[1] < num[2]:
    menor = num[1]
elif num[2] < num[1] and num[2] < num[0]:
    menor = num[2]
if num[1] > num[0] and num[1] > num[2]:
    maior = num[1]
elif num[2] > num[1] and num[2] > num[0]:
    maior = num[2]
print(f'O maior valor é {cores.vermelho}{maior}{cores.nenhum}, e o menor é {cores.azul}{menor}{cores.nenhum} usando if, elif.')