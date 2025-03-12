# listas, variaveis compostas.
# lista = [var1, var2, ...]
lista = list()
lanche = ["Hamburger", "Suco", "Pizza", "Pudím"] # inicializando uma lista
print(lanche)
print(lanche[2]) # lista pode ser fatiada como strings.
print(lanche[1][3]) # strings dentro de listas fatiada.
lanche.append("Sorvete") # adicionando "Sorvete" para ao final lista
print(lanche)



lanche.insert(0, "cookie") # inserindo um novo item no índice 0
                                          # todos os itens deste índice em diante são movidos.
                                          # 1 índice para frente
print(lanche)
del lanche[1] # outro jeito de remover um item da lista no índice 1
print(lanche)
lanche.pop(3)  # removendo um item da lista no índice 3
print(lanche)
lanche.remove("Pizza")  # este metodo remove a string "Pizza" da lista
print(lanche)
lanche.pop()  # remove o ultimo elemento
print(lanche)
lanche.clear() # limpando a lista inteira
print(lanche)

valores = list(range(4, 14))
valores2 = [22,54,46,74,3,1]
print(valores)
print(valores2)
valores2.sort() # usando o metodo sort() na lista para arranja-la em ordem crescente
print(valores2)
valores2.sort(reverse=True) # inverte a ordem de sort() em ordem decrescente
print(valores2)
print(len(valores2))
valores[4] = 11 # reassinando valores é possivel
print(valores)
# mas tentar adicionar um valor como abaixo não é
# valores[11] = 12
valores.append(12) # o metodo append() tem que ser usado para adicionar um valor
print(valores)

numeros = list()
for cont in range(5):
    numeros.append(int(input("Digite um numero: ")))
for indice, valor in enumerate(numeros):
    print(f"indice {indice} = {valor}...")

lista1 = valores # ligando uma lista com a outra, se uma lista mudar, ambas serao.
print(f'lista antes da mudança {lista1} {valores}')
lista1[0] = 999 # seja a lista ligada a ser mudada.
print(f'lista depois da mudança {lista1} {valores}')
valores[4] = 888 # ou a lista original.
print(f'lista depois de mais uma mudança {lista1} {valores}')

lista2 = valores2[:] # assina apenas os valores da lista 'valores2' a lista 'lista2'
print(f'lista antes da mudança {lista2} {valores2}')
lista2[0] = 999 # assim eu posso mudar uma lista
print(f'lista depois da mudança {lista2} {valores2}')
valores2[4] = 888 # sem mudar a outra.
print(f'lista depois de mais uma mudança {lista2} {valores2}')