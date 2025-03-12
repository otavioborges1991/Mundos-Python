# refaça o ex051 usando while
import caixastr

print("Gerando progressão aritmética.")
primeiro = int(input("Primeiro termo: "))
razão = int(input('Razão: '))
termos =int(input('Termos: '))
progressão = primeiro + (termos) * razão

# progressão aritmética com for loops do ex051
caixastr.caixa("Progressão artmética com for loop")

for i in range(primeiro, progressão, razão):
    print(f'{i} ->', end=" ")

print("Acabou!")

# mesma progressão agora em while loop
caixastr.caixa("Agora com while loop")

i = primeiro
while i < termos * razão:
    print(f'{i} ->', end=" ")
    i += razão

print("Acabou!")