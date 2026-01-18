# Leia vários números inteiros. No final mostre a média, o maior e o menor.
# O programa pergunta o usuário se ele quer continuar. Sim/Não.

# inicializando variáveis
números = []
continuar = "S"
soma = 0
média = 0
maior = 0
menor = 0

while True: # while True significa loop infinito
            # condições no loop com um break é a única coisa que faz esse loop parar.

    if continuar == 'S':
        números.append(int(input("Digite um número: ")))
    elif continuar == 'N':  # se a variável continuar conter a letra N
        break               # sai do loop.
    else:
        print("Resposta invalida.")
    continuar = input("Quer continuar:  [S]im/[N]ão: ").strip().upper()[0]


soma = sum(números)
média = soma / len(números)
maior = max(números)
menor = min(números)

print(f'''
Analisando dados
Números: {números}
Média: {média:.2f}
Soma: {soma}
Maior: {maior}
Menor: {menor}
''')


