# Leia um ano e mostre se é bissexto.
import cores

from datetime import date
print('Vamos ver se o ano é bissexto')
ano = int(input('Digite um ano, ou digite 0 para analizar ano atual: '))

if ano == 0:
    ano = date.today().year

print(f"Analisando ano {cores.fmagenta}{cores.vermelho}{ano}{cores.nenhum}")
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Ano {cores.sublinhado}é bissexto')
else:
    print(f'ano {cores.sublinhado}não é bissexto')

