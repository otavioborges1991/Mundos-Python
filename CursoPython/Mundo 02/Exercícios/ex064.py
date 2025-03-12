# Leia números inteiros entre 0 e 999, o programa só para quando ler o número 999.
# mostre quantos números foram digitados e a soma entre eles.
# desconsidere o flag "999" ao contar um numeros e soma.
escolha = 0
números = []
while True:
    escolha = int(input("Digite um numero inteiro entre 0 e 998 (999 sai do programa): "))
    if escolha == 999:
        break
    números.append(escolha)

soma = sum(números)
valores = len(números)
print(f'Ao todo foram {valores} números digitados, a soma entre eles é {soma}')
