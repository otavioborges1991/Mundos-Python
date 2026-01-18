# Tuplas são variaveis compostas, "imutáveis"
lanches = "Hamburger", "Suco", "Pizza", "Pudím"
# a linha abaixa esta tentando mudar a tupla
# lanches[1] = "Refrigerante"
# esta também, mas essa funciona
# lanches = "OI"
print(type(lanches))

# Variavéis compostas podem ser iteradas em loops
for comida in lanches: # iterando items em uma tupla
    print(f'Eu vou comer {comida}.')

print(f"{sorted(lanches)}") # função sorted mostre variaveis compostas.
                            # em order sem alterar a tupla, lista ou dicionário.


# e fatiadas como strings
print(lanches)
print(lanches[2])
print(lanches[1:3])
print(lanches[-1])
print(lanches[-3:])

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # junta as duas tuplas em uma tupla.
d = 15
e = 30
f = (d, e) # faz uma tupla contendo os numeros das duas variaveis
print(f)
print(c.count(2)) # Metodo count(num) retorna quantas vezes o num apareceu nesta tupla
print(c.index(8)) # Metodo index(num) retorna o indice do num.
print(c.index(5,2)) # retorn o valor apartir do indice 2
# reassignar as variaveis 'd' e 'e' não vai mudar a tupla 'f'
d = 20
e = 10
print(f)

pessoa = ("Otavio", 39, "M", 65.5) # diferentes tipos de dados podem ser usados em uma tupla
print(pessoa)
del pessoa  # comando del() apaga a tupla, poderia ser usado em um indice, mas tuplas não mudam
            # Usar a variável "pessoa" depois do del não funcionaria.
#print(pessoa)
