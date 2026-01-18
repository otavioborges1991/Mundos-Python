# leia o primeiro termo e a razão duma progressão aritmética, no final mostre os 10 primeiros
# termos.

print("Gerando progressão aritmética.")
inicio = int(input("Inicio: "))
razão = int(input('Razão: '))
termos = inicio + (10 - 1) * razão
for i in range(inicio, termos, razão):
    print(f'{i} ->', end=" ")
print("Acabou!")