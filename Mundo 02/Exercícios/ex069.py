# Leia a idade e sexo de várias pessoas, a cada pessoa pergunte para continuar.
# No final mostre:
# Quantas maiores de 18 anos.
# Quantos homens.
# Quantas mulheres com menos de 20.

sexo = "N/A"
maiores_de_idade = 0
homens = 0
mulheres_menores = 0
pessoas = 0

print("Cadastrando pessoas")

while True:
    pessoas += 1

    # validando idade
    while True:
        idade = (int(input("Digite a idade: ")))
        if idade >= 0:
            break
        else:
            print("Idade invalida")

    # validando sexo
    while True:
        sexo = str(input("Sexo, masculino ou feminino. M/F: ")).strip().upper()[0]
        if sexo not in "MF":
            print("Sexo invalido")
        else:
            break

    # checando quantos são maiores de idade
    if idade >= 18:
        maiores_de_idade += 1

    if sexo == "M":             # checando quantos são homens
        homens += 1             # e os quais não são homens...
    elif idade < 20:            # checa se são menores de 20 anos.
        mulheres_menores += 1

    # perguntando se quer continuar
    while True:
        continuar = str(input("Continuar Sim, Não S/N: ")).strip().upper()
        if continuar not in "SN":
            print("Escolha invalida")
            continue
        else:
            break

    if continuar == "N":
        break

print(f"""Das {pessoas} pessoas registradas {maiores_de_idade} são maiores de idade.
{homens} são homens e {mulheres_menores} mulheres tem menos de 20 anos.""")