# leia o peso de 5 pessoas, mostre qual o maior e o menor
from xml.sax.saxutils import prepare_input_source

import caixastr

maior = 0
menor = 0
pesos = []

caixastr.caixa("Lendo pesos de 5 pessoas e mostrando maior e menor")


# tirando o maior e o menor peso usando for loop
for p in range(0, 5):
    pesos.append(float(input('Digite um peso: Kg')))
    if p == 0:
        menor = maior = pesos[p]
    if pesos[p] > maior:
        maior = pesos[p]
    elif pesos[p] < menor:
        menor = pesos[p]

print(f'A lista de pesos contém {pesos}.')
print(f'Destes o maior é {maior} e o menor {menor} de acordo com o for loop')
# Fazendo a mesma coisa mas usando a função max() e min()
maior = max(pesos)
menor = min(pesos)
print(f'Destes o maior é {maior} e o menor {menor} de acordo com as funçoes max() e min()')