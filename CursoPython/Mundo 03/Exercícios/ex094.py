# Leia o nome, sexo e idade de várias pessoas. Guardando cada num dicionário.
# e todos os dicionários numa lista. No final mostre:
# A) quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres
# D) uma lista com todas as pessoas com idade acima da média.

pessoa = dict()
pessoas = list()
sexo = "Z"
média = 0
mulheres = []
acima_da_média = []
print("Cadastrando pessoas")
while True:
    # Perguntando se quer adicionar mais uma pessoa
    resposta = str(input("Quer adicionar uma pessoa S/N: ")).strip().upper()[0]
    if resposta not in "SN":
        print("Resposta invalida, digite apenas S para sim ou N para não.")
        continue
    elif resposta in "N":
        break

    nome = " ".join(str(input('Nome: ')).strip().title().split())

    while True:
        sexo = str(input("Sexo M/F: ")).strip().upper()[0]
        if sexo in "MF":
            break
        else:
            print('Sexo Invalido')
    idade = int(input("idade: "))
    pessoa = {'nome': nome, 'sexo': sexo, 'idade': idade}
    pessoas.append(pessoa)
    # encontrando todas as mulheres da lista
    if sexo == "F":
        mulheres.append(len(pessoas) - 1) # isso me da o indice das mulheres na lista pessoas
    # reiniciando respostas para uso no próximo loop
    resposta = "z"
    sexo = "Z"

if len(pessoas) == 0:
    exit("Nenhuma pessoa adicionada a lista")

total_de_pessoas = len(pessoas)
média = sum(map(lambda item: item['idade'], pessoas)) / total_de_pessoas


print(f'''\nAnalisando a lista:
total de pessoas cadastradas = {total_de_pessoas}
média de idade do grupo = {média:.1f}
\nA lista de todas as mulheres:''')

for indice in mulheres:
    for chave, valor in pessoas[indice].items():
        if chave == "sexo":
            continue
        print(f"{chave}:{valor}", end=" ")
    print()

for pessoa in pessoas:
    if pessoa['idade'] > média:
        acima_da_média.append(pessoa)
print("\nA lista com as pessoas de idade acima da média")
for pessoa in acima_da_média:
    for chave, valor in pessoa.items():
        if chave == 'sexo' and valor == "F":
            valor = "Feminino"
        elif chave == 'sexo' and valor == "M":
            valor = "Masculino"
        print(f'{chave}:{valor}', end=" ")
    print()