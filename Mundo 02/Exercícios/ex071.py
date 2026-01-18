# Crie um programa simulando um caixa eletrônico.
# Pergunto o valor a sacar (número inteiro).
# O programa informa quantas cédulas de cada valor a se entregar.
# Cédulas de 50, 20, 10 e 2 reais.



conta_corrente = 5000.00
print("Programa caixa eletrônico")
while True:
    # zerando notas a ser entregue
    nota100 = 0
    nota50 = 0
    nota20 = 0
    nota10 = 0
    nota2 = 0

    print(f"Saldo R${conta_corrente}")
    # validando saldo suficiente
    while True:
        saque = int(input("Quanto dinheiro sacar R$"))
        if saque > conta_corrente:
            print("Voce não tem saldo o suficiente.")
        else:
            conta_corrente -= saque - (saque % 2)
            break

    # Calculando quantas notas devolver ao usuário.
    while True:
        if saque >= 100:
            nota100 += 1
            saque -= 100
        elif saque >= 50:
            nota50 += 1
            saque -= 50
        elif saque >= 20:
            nota20 += 1
            saque -= 20
        elif saque >= 10:
            nota10 += 1
            saque -= 10
        elif saque >= 2:
            nota2 += 1
            saque -= 2
        else:
            break


    # Devolvendo notas
    print(f'''
Você recebe.
{nota100} notas de R$100 reais
{nota50} notas de R$50 reais
{nota20} notas de R$20 reais
{nota10} notas de R$10 reais
{nota2} notas de R$2 reais
''')
    # validando continuar o saque ou para
    while True:
        continuar = str(input("Continuar a sacar S/N: ")).strip().upper()[0]
        if continuar not in "SN":
            print("Escolha inválida.")
        else:
            break
    if continuar == "N":
        break
