# Leia dois números inteiros e compare-os, mostre uma mensagem
# - O primeiro valor é maior.
# - O segundo é o maior.
# - Nenhum valor é maior que o outro
import cores


print("distinguindo maior do menor entre 2 números.")
numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))

if numero1 > numero2:
    print(f"O {cores.sublinhado}primeiro{cores.nenhum} valor é maior.")
elif numero2 > numero1:
    print(f"O {cores.sublinhado}segundo{cores.nenhum} valor é maior.")
else:
    print(f"Ambos os valores são {cores.azul}iguais{cores.nenhum}.")