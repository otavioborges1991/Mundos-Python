# leia um número inteiro e diga se ele é um número primo.
import cores

import caixastr
caixastr.caixa("Checando número primo.")
número = int(input("Digite um numero inteiro: "))
primo = True
print(f'{cores.verde}1', end=" ")
for i in range(2, número):
    if número % i == 0:
        primo = False
        print(f'{cores.vermelho}{i}', end=" ")
    else:
        print(f'{cores.azul}{i}', end=" ")

print(f"{cores.verde}{número}{cores.nenhum}\nO numero é primo? {cores.amarelo}{cores.piscando}{primo}")