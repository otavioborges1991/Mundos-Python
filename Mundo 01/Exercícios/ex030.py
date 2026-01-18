# leia um número e mostre se ele é par ou ímpar.
import cores

num = int(input('Digite um número: '))
if num % 2 == 0:
    print(f'Ele é {cores.verde}par')
else:
    print(f'Ele é {cores.azul}ímpar')