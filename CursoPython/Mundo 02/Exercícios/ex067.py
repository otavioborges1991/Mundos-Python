# Mostre a tabuada de vários números, um de cada vez.
# Números negativos é flag de parada.

print("Fazendo tabuada.")
while True:
    número = int(input("Digite um número [negativos para encerrar]: "))
    if número < 0:
        break
    for n in range(1, 11):
        print(f"{número} x {n} = {número * n}")
