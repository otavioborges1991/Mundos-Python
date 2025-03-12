# Leia o nome e peso de varias pessoas e coloque em uma lista
# no final mostre, quantos pessoas cadastradas
# uma lista com as pessoas mais pesadas
# uma com as mais leves

nomes = []
pesos = []
pessoas = [nomes, pesos]


resposta = "S"
pesados = []
leves = []
print("Cadastrando nomes e pesos")

while True:
    resposta = str(input("Adicionar novo? S/N: ")).strip().upper()[0]
    # validando respsosta.
    if resposta not in "SN":
        print("Resposta invalida")
        continue
    elif resposta == "N":
        break

    # perguntando nome e peso
    nome = " ".join(str(input("Nome: ")).strip().upper().title().split())
    peso = float(input("Peso: "))

    # adicionando nome a lista
    nomes.append(nome)

    # validando mais pesados da lista
    # se for o primeiro da lista o peso é adicionada a lista de pesos antes de testes de mais pesados ou leves
    # o primeiro nome tambem é adicionado a lista de leves e pesados junto com seu peso
    if len(nomes) == 1:
        pesos.append(peso)
        pesados.append(peso)
        pesados.append(nome)
        leves.append(peso)
        leves.append(nome)

    else:

        # validando o mais pesado
        if peso > max(pesos):      # se o peso é maior que o mais pesado, ou for o primeiro da lista
            pesados.clear()        # a lista é zerada
            pesados.append(peso)   # peso é adicionados a lista pesados
            pesados.append(nome)   # nome também
        elif peso == max(pesos):   # se o peso da pessoa atual a ser analisado é igual ao mais pesado da lista
            pesados.append(nome)   # o nome desta pessoa é adicionado a lista pesados

        # validando os mais leves da lista
        if peso < min(pesos):      # se for mais leve que o mais leve da lista, ou o primeiro da lista
            leves.clear()          # a lista zera.
            leves.append(peso)     # o peso é adicionado a lista leves
            leves.append(nome)     # nome também
        elif peso == min(pesos):   # se o peso for igual ao mais leve
            leves.append(nome)     # o nome desta pessoa é adicionada a lista leves

        # peso é adicionada depois de testa mais leve e mais pesados devido a como o teste é feito
        pesos.append(peso)

print(f"Pessoas cadastradas:")
for pessoa in pessoas[0]:
    print(pessoa)
print(f"""
Os mais pesados foram {pesados[1:]} pesando {pesados[0]}
e os mais leves foram {leves[1:]} pesando {leves[0]}""")