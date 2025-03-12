# Leia 2 valores e mostre um menu na tela
# 1 somar, 2 multiplicar, 3 maior, 4 novos números, 5 sai do programa.

valor1 = 0
valor2 = 0

escolha = 4
while escolha != 5:

    if escolha == 1:
        print(f"Soma: {valor1} + {valor2} = {valor2+valor1}")
    elif escolha == 2:
        print(f"Multiplicação: {valor1} * {valor2} = {valor1*valor2}")
    elif escolha == 3:
        print(f"Maior entre {valor1} e {valor2} é {max(valor2, valor1)}")
    elif escolha == 4:
        valor1 = float(input("Digite um numero: "))
        valor2 = float(input("Digite outro numero: "))
    elif escolha == 5:
        break
    else:
        print("Opção invalida!")

    print(f"""
    [1] somar.
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    """)
    escolha = int(input("Escolha: "))
