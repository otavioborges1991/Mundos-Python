# leia 6 números e mostre a soma dos numeros pares.

números = []
soma_dos_pares = 0
for i in range(0, 6):
    números.append(int(input(f"{i + 1} Digite um numero: ")))
    if números[i] % 2 == 0:
        soma_dos_pares += números[i]

print(f"Os números digitados foram {números}.\n"  # outras forma de usar strings em múltiplas linhas
      f"A soma dos pares desta lista resulta em {soma_dos_pares}") # não pula a linha sem usar \n