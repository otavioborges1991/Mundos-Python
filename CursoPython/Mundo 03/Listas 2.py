# listas dentro de listas

dados = list()
dados.append('Pedro Alvares Cabral')
dados.append(25)

print(dados)
pessoas = list()
pessoas.append(dados) # append() adiciona todos os elementos da lista dados como um único elemento

print(pessoas)

lista = []
lista.extend(pessoas) # extend() adiciona todos os elementos de uma lista
                      # como elementos separados. ao contrario de append()
print(lista)

pessoas = [['Pedro', 25],['Maria', 19],['João', 32],['Otávio Vínicios Borges', 34]]
print(pessoas)       # escreve a lista inteira
print(pessoas[1])    # fatiando a lista vai mostrar a lista dentro da lista
print(pessoas[0][0]) # fatiando a lista dentro da lista
print(pessoas[1][1])
print(pessoas[2][0])

for pessoa, idade in pessoas: # pegando nome e idade separados não é obrigatíro
    print(f"A Pessoa de nome {pessoa} tem {idade} anos de idade")

for pessoa in pessoas: # escreve todos os dados de uma só vez
    print(f"Individuo {pessoa}.")

# exemplo de um for loop iterando numa lista com listas dentro
for pessoa, idade in pessoas:
    if idade >= 20:
        print(f'{pessoa} é maior de idade')
    else:
        print(f"{pessoa} não é maior de idade")