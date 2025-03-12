# Usuário digita uma expressão matemática que use parenteses.
# Análise se a expressão está com os parenteses abertos e fechados na ordem correta

# a variável parenteses acompanha os parenteses abertos e fechados, incrementando para cada aberto
# e decrementando para cada fechado. Se em algum ponto do loop o numero em parenteses for negativo
# significa que mais parenteses foram fechados do que abertos, por tanto, a expressão a ser analisada
# esta incorreta. Se no final do loop o numero em parenteses ainda estiver positivo, significa que
# mais parenteses foram abertos do que fechados.
parenteses = 0
while True:
    expressão = str(input("Digite uma expressão matematica: "))
    # analisando a expressão
    for iteração, letra in enumerate(expressão):
        if letra == '(':
            parenteses += 1
        elif letra == ')':
            parenteses -= 1
        if parenteses < 0:
            print("Expressão invalida.")
            break
        if iteração == len(expressão) - 1 and parenteses !=0:
            print("Expressão invalida.")
        elif iteração == len(expressão) - 1:
            print("Expressão valida")
    resposta = "?"

    while resposta not in "SN":
        resposta = str(input("Quer tentar de novo, escreva sim ou não? ")).strip().upper()[0]
    if resposta == "S":
        continue
    else:
        break


