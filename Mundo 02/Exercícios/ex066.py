# Leia vários números inteiros. 999 é o flag para parar.
# Mostre qual foi a soma desconsiderando o flag.

número = 0
números = []

while True:
    número = int(input("Digite um número (999 finaliza o programa): "))
    if número == 999:
        break
    números.append(número)

print(f'Os números digitados foram {números}, a soma deles é {sum(números)}')